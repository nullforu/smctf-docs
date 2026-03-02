---
title: 환경 변수 설정
sidebar:
    order: 10
---

Container Provisioner는 SMCTF와 마찬가지로 다양한 환경 변수 옵션을 지원합니다. 내부 전용 마이크로서비스이기 때문에 CORS 관련 설정은 필요하지 않습니다.

### Application

```ini
# App
APP_ENV=local
HTTP_ADDR=:8081
SHUTDOWN_TIMEOUT=10s
```

Container Provisioner 애플리케이션의 전반적인 설정을 구성하는 환경변수로, 실행 환경이나 HTTP 서버 주소와 포트, Graceful shutdown 타임아웃 등을 설정할 수 있습니다.
기본 포트는 8081입니다.

### API Key

```ini
# AuthN
API_KEY_ENABLED=true
API_KEY=secret
```

마이크로서비스 간 인증을 위해 API Key 방식을 사용할 수 있습니다. 이때 위 옵션을 적절히 설정하세요.

### Logging

```ini
# Logging
LOG_DIR=logs
LOG_FILE_PREFIX=app
LOG_MAX_BODY_BYTES=1048576
```

기본적으로 Container Provisioner는 JSON으로 구조화된 로그를 stdout/stderr로 출력하며, 시간대별로 로그 파일을 분리하여 저장하는 Rotating 로깅이 구현되어 있습니다.

자세한 내용은 인프라 문서의 [로깅 및 모니터링](/infra/observability) 문서를 참조하세요.

### Stack provisioning

```ini
# Stack provisioning
STACK_NAMESPACE=stacks
STACK_TTL=2h
STACK_SCHEDULER_INTERVAL=10s
STACK_NODEPORT_MIN=31001
STACK_NODEPORT_MAX=32767
STACK_PORT_LOCK_TTL=30s
STACK_NODE_ROLE=stack
STACK_REQUIRE_INGRESS_NETWORK_POLICY=true
```

스택 프로비저닝과 관련된 전반적인 설정입니다.
가장 핵심적인 설정으로, 스택이 배치될 네임스페이스와 스택 TTL, 루프 간격, NodePort 범위와 NodeSelector 등을 설정합니다.

적절히 조정하여 사용하세요.

### DynamoDB

```ini
# DynamoDB
DDB_USE_MOCK=false
DDB_STACK_TABLE=smctf-stacks
DDB_CONSISTENT_READ=true
AWS_REGION=ap-northeast-2
AWS_ENDPOINT=
```

스택 메타데이터 저장을 위한 DynamoDB 클라이언트 설정입니다.
`DDB_USE_MOCK`은 개발 환경이나 테스트 환경에서 활성화하여 사용하세요. 프로덕션 환경에선 절대 권장하지 않습니다.

### Kubernetes

```ini
# Kubernetes
K8S_USE_MOCK=false
K8S_KUBECONFIG=
K8S_CONTEXT=
K8S_CLIENT_QPS=20
K8S_CLIENT_BURST=40
STACK_SCHEDULING_TIMEOUT=20s
```

스택 프로비저닝을 위한 Kubernetes 클라이언트 설정입니다.
`K8S_USE_MOCK`은 오로지 테스트 환경에서 활성화하여 사용하세요. 정상적인 동작이 불가능한 설정입니다.

`K8S_KUBECONFIG`와 `K8S_CONTEXT`는 클러스터 외부에서 실행되는 경우에만 필요합니다.
클러스터 내부에서 실행되는 경우 InCluster Config를 사용하므로 별도로 자격증명을 필요로하지 않습니다.

그 외의 설정은 필요에 따라 적절히 조정하세요.
