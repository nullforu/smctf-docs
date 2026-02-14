---
title: 20. 설치 및 Dockerfile 구성
sidebar:
    order: 120
---

SMCTF는 Go 언어로 작성된 애플리케이션으로, Docker를 사용하여 쉽게 배포할 수 있도록 Dockerfile이 제공됩니다. 

스택 기능을 사용할 경우 [Container Provisioner](/container-provisioner)와 함께 사용해야 하며, 이 또한 Dockerfile을 통해 컨테이너 이미지로 빌드할 수 있습니다.

이 문서는 로컬에서 테스트 용도로 SMCTF를 설치하고 구성하는 방법을 설명합니다. 실제 배포 환경에서는 EKS Kubernetes 클러스터와 같은 컨테이너 오케스트레이션 플랫폼을 사용하며, 이는 추후 별도의 문서에서 다룰 예정입니다.

### Dockerfile

기본 Dockerfile은 아래와 같습니다. [Container Provisioner](/container-provisioner)에선 `frontend` 디렉토리를 포함하여 빌드하도록 Dockerfile이 구성되어 있습니다.

```Dockerfile
ARG GO_VERSION=1.25.5

FROM golang:${GO_VERSION} AS build
ARG TARGETOS=linux
ARG TARGETARCH=amd64
WORKDIR /src

COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod \
    go mod download

COPY . .

RUN --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 GOOS=${TARGETOS} GOARCH=${TARGETARCH} \
    go build -trimpath -ldflags="-s -w" -o /out/server ./cmd/server

RUN mkdir -p /out/logs
FROM gcr.io/distroless/base-debian12
WORKDIR /app

COPY --from=build /out/server /app/server
COPY --from=build --chown=nonroot:nonroot /out/logs /app/logs

ENV HTTP_ADDR=:8081 \
    LOG_DIR=/app/logs

EXPOSE 8080 # for smctf server, if you use container provisioner, also expose 8081 for stack server
USER nonroot:nonroot
ENTRYPOINT ["/app/server"]
```

### 빌드 및 실행

SMCTF, Container Provisioner 및 [smctfe(프론트엔드)](https://github.com/nullforu/smctfe)를 모두 다운받고 빌드하려면, 루트 디렉토리에서 아래 명령어를 실행하세요.

```bash
git clone https://github.com/nullforu/smctf.git
git clone https://github.com/nullforu/smctfe.git
git clone https://github.com/nullforu/container-provisioner-k8s.git
```

각각의 프로젝트에서 Docker 이미지를 빌드하려면, 각 디렉토리에서 아래 명령어를 실행하세요.

```bash
docker build -t smctf:latest .
docker build -t smctfe:latest ./smctfe
docker build -t container-provisioner:latest ./container-provisioner-k8s

# or buildx for multi-arch support
docker buildx build --platform linux/amd64,linux/arm64 -t smctf:latest .
docker buildx build --platform linux/amd64,linux/arm64 -t smctfe:latest ./smctfe
docker buildx build --platform linux/amd64,linux/arm64 -t container-provisioner:latest ./container-provisioner-k8s

# or push to ecr registry (need to set up aws cli and ecr auth)
# ECR_URI=123456789012.dkr.ecr.region.amazonaws.com/repository (example)
docker buildx build \
    --platform linux/amd64,linux/arm64 \
    -t "${ECR_URI}:latest" \
    --push \
    .
```

빌드된 이미지를 간단하게 Docker compose 등으로 실행할 수 있습니다. PostgreSQL과 Redis는 아래의 Docker compose를 참고하세요.

```yaml
version: "3.9"

services:
  postgres:
    image: postgres:16
    container_name: local-postgres
    restart: unless-stopped
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - local-net

  redis:
    image: redis:7
    container_name: local-redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    command: ["redis-server", "--appendonly", "yes"]
    volumes:
      - redis_data:/data
    networks:
      - local-net

volumes:
  postgres_data:
  redis_data:

networks:
  local-net:
    driver: bridge
```

Docker를 통해 빌드하지 않고 로컬에서 직접 빌드하고 실행하려면 Go 및 NodeJS/NPM 환경이 필요합니다.

```bash
# smctf server, container provisioner
go mod download
go build -o server ./cmd/server
./server

# or go run ./cmd/server for development

# smctfe frontend
cd smctfe
npm install
npm run build
npm run preview # or npm run dev for development
```

### 로컬 Kubernetes 구성

인프라 구성은 Terraform 및 Kubernetes 매니페스트로 관리되기 때문에 로컬에서는 테스트 용도로 Minikube 또는 KinD를 사용하여 Kubernetes 클러스터를 구성할 수 있습니다. (KinD를 권장합니다.)

KinD 클러스터 구성은 아래와 같으며, 이에 대한 자세한 내용은 [nullforu/container-provisioner-k8s](https://github.com/nullforu/container-provisioner-k8s) 문서를 참고하세요.

```yaml
# kubernetes/cluster/kind.dev.yaml

kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
```

```bash
kind create cluster --name dev --config=kubernetes/cluster/kind.dev.yaml
```

자세한 내용은 생략합니다. 본 프로젝트를 이러한 방식으로 프로덕션에서 운영하는 것은 절대 권장하지 않습니다. 이는 테스트 용도임을 명심하세요.

### 관리자 역할 부여

아래의 PostgreSQL 쿼리를 통해 기존 계정에 관리자 역할을 부여할 수 있습니다.

```sql
-- INSERT INTO users (email, username, password_hash, role, team_id, created_at, updated_at) VALUES ('admin@smctf.com', 'admin', '$2b$12$5AajwaaA4.H9W..MEM7mT.QkxeyxXqUTLjpPLvjhXhWm8glrpcUcG', 'admin', 1, '2026-02-11 12:03:00', '2026-02-11 12:03:00');
UPDATE users SET role='admin' WHERE email='admin@smctf.com';
```

관리자 계정을 처음으로 생성하는 방법은 SQL로 팀과 가입 인증 키를 생성한 후 UI에서 회원가입 후 다시 위 쿼리를 통해 해당 계정에 관리자 역할을 부여하는 방법이 있습니다. 

```sql
INSERT INTO teams (name) VALUES ('Admin Team');

INSERT INTO registration_keys (code, created_by, team_id) VALUES ('000000', 0, 1);
-- 000000 가입 인증 키로 가입 후 계정 생성
UPDATE users SET role='admin' WHERE email='생성된_관리자_계정_이메일';
--- 로그아웃 후 다시 로그인해야 관리자 권한이 적용됩니다.
DELETE FROM registration_keys WHERE code='000000';
```

관리자 계정을 SQL 쿼리로 직접 생성할 수도 있지만, Bcrypt 해시된 비밀번호를 생성하는 과정이 필요하기 때문에 위 방법을 권장합니다. 
