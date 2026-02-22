---
title: 1. 도커 이미지 빌더
sidebar:
    order: 1
---

로컬에서 직접 도커 이미지를 빌드하기 어려운 환경(예: ARM 아키텍처 혹은 제한된 리소스/네트워크 환경)에서도 쉽게 도커 이미지를 빌드할 수 있도록 Github Actions 기반의 도커 이미지 빌더를 제공합니다. 

구성 방법 또는 사용 방법은 아래의 레포지토리에 설명되어 있습니다. 소스로는 레포지토리 내에 포함된 ZIP 파일을 지정하거나 AWS S3 버킷의 객체 키를 지정할 수 있습니다. (후자는 S3 GetObject IAM 권한이 필요합니다. 이 또한 설명되어 있습니다.)

- https://github.com/nullforu/docker-image-builder

이는 SMCTF 프로젝트와는 무관하지만, 스택을 제공해야하는 문제들은 모두 도커 이미지로 ECR에 배포되어야 하므로 해당 워크플로우를 통해 쉽게 배포할 수 있도록 제공합니다.

### Example Dockerfile

리버싱 등의 문제에서 Netcat과 같은 도구를 사용해야하는 경우가 있습니다. 예시로 아래의 Dockerfile을 통해 Netcat이 포함된 이미지를 빌드할 수 있습니다.

- 문제 예시 출처: https://dreamhack.io/wargame/challenges/836

```
> tree .
.
├── chall
├── Dockerfile
└── flag
```

```Dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y socat \
    && useradd -m ctf

WORKDIR /home/ctf

COPY chall /home/ctf/chall
COPY flag /home/ctf/flag

RUN chown -R root:ctf /home/ctf \
    && chmod 750 /home/ctf \
    && chmod 550 /home/ctf/chall \
    && chmod 440 /home/ctf/flag

USER ctf

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/home/ctf/chall
```

로컬에서 직접 빌드할 필요 없이 Dockerfile이 포함된 프로젝트 압축 후 S3에 업로드하거나 레포지토리에 올려 Github Actions 워크플로우를 통해 쉽게 빌드하여 ECR에 배포할 수 있습니다.

S3 버킷 사용을 권장합니다. 레포지토리에 올리는 경우 민감한 정보가 포함되지 않도록 주의하세요. 실제로 사용 시 프라이빗 레포지토리를 사용하는 것을 권장합니다. (단, 요금 발생에 주의하세요.)
