---
title: Infrastructure Changelog
sidebar:
    order: 3
---

## v1.0.0 (2026-02-22)

SMCTF 인프라 아키텍처에 대한 첫번째 구현이자 첫번째 공식 릴리즈입니다. [SMCTF v1.2.0](/changelog) 및 [Container Provisioner v1.1.0](/changelog/container-provisioner)과 호환되며, 암묵적으로 [Frontend v1.0.0](/changelog/frontend)과도 호환됩니다.

아키텍처는 AWS 및 Kubernetes를 기반으로 구축되었으며, 자세한 내용은 [인프라 문서](/infra)에서 확인할 수 있습니다.

```md
See https://ctf.null4u.cloud/changelog for more details.

This release is compatible with [SMCTF v1.2.0](https://github.com/nullforu/smctf/releases/tag/v1.2.0) and [Container Provisioner v1.1.0](https://github.com/nullforu/container-provisioner-k8s/releases/tag/v1.1.0).

## What's Changed
* The foundational infrastructure has been established, including Terraform based IaC and Kubernetes manifests/Helm chart. (Please refer to the attached image for the architecture.)
* Add FluentBit for AWS CloudWatch and Prometheus Stack by @yulmwu in https://github.com/nullforu/smctf-infra/pull/1

## New Contributors
* @yulmwu made their first contribution in https://github.com/nullforu/smctf-infra/pull/1

**Full Changelog**: https://github.com/nullforu/smctf-infra/commits/v1.0.0
```
