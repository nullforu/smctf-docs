---
title: 개요
sidebar:
    order: 1
---

SMCTF의 주요 모토(슬로건)은 누구나 쉽게 배포하여 사용할 수 있는 CTF 플랫폼을 만드는 것입니다.
여기엔 암묵적으로 보안성 및 확장성, 가용성이 포함되어 있고 이를 달성하기 위해 SMCTF는 Terraform(AWS Provider) 및 Kubernetes Helm을 통해 쉽게 AWS 인프라를 배포할 수 있도록 설계되었습니다.

이 문서에서는 SMCTF에서 제공하는 인프라와 이를 배포하는 방법에 대해 설명합니다. 이에 대해선 전반적으로 아래의 레포지토리에 의존합니다.

- https://github.com/nullforu/smctf-infra

이 레포지토리엔 Terraform HCL 및 Kubernetes Helm 차트가 포함되어 있으며, 몇몇 구성만 수정한다면 바로 배포하여 사용할 수 있도록 설계되었습니다. 자세한 내용은 다음 문서를 참조하세요.

---

![AWS Architecture](architecture/aws.drawio.png)

![Kubernetes Architecture](architecture/k8s.drawio.png)

<!--
-. Overview
-. AWS
-. K8s
-. Terraform
-. Helm
-. Observability
-->
