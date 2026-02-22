---
title: Container Provisioner Changelog
sidebar:
    order: 2
---

## v1.1.0 (2026-02-22)

아래와 같은 개선 및 기능이 추가되었습니다. `v1.0.0`과 호환되며 [SMCTF v1.2.0](/changelog), [Infrastructure v1.0.0](/changelog/infra)과 호환됩니다.

---

- JSON으로 구조화된 로깅을 지원하며 OpenMetrics 엔드포인트(`/metrics`)가 추가되었습니다. 이에 따라 로깅 및 모니터링 시스템이 크게 변경되었으며 더 이상 Discord/Slack 웹훅 로깅을 지원하지 않습니다. 이는 보안상의 이유도 있다고 판단하였기 때문에 이전 버전과 호환되지 않는 변경 사항입니다.
- 자세한 내용은 인프라 문서의 [로깅 및 모니터링](/infra/6-observability) 문서를 참조하세요. PR [10](https://github.com/nullforu/container-provisioner-k8s/pull/10)

---

- 몇몇의 버그 수정과 함께 내부적으로 코드 리팩토링이 이루어졌습니다.

## v1.0.0 (2026-02-07)

```md
## What's New/Changed

We believe that the majority of the Container Provisioner’s functionality has now been implemented. As a result, development of the Container Provisioner will be paused at this point, and focus will shift to developing the REST APIs and business logic for Stack creation in [SMCTF](https://github.com/nullforu/smctf).

Although validation and testing of this project are not yet complete, testing is deferred for now due to the practical difficulty of setting up and provisioning real DynamoDB resources and Kubernetes clusters for testing purposes.

Documentation for this microservice will also be consolidated into a single document and provided at a later time. For now, please refer to the source code directly. Thank you.

* v1.0.0 release – 2026/02/07

**Full Changelog**: https://github.com/nullforu/container-provisioner-k8s/commits/v1.0.0
```
