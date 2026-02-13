---
title: 4. TTL 및 스케줄러
sidebar:
    order: 4
---

Container Provisioner는 내부적으로 DynamoDB를 통해 스택과 관련된 메타데이터를 관리합니다. 때문에 DDB의 메타데이터와 쿠버네티스의 클러스터 상태가 일치하지 않을 경우가 있을 수 있고,
이는 곧 Orphaned 스택 Pod를 만들어 리소스를 낭비하는 결과를 초래할 수 있습니다. 이를 방지하기 위해 Container Provisioner는 주기적으로 DDB와 쿠버네티스 클러스터 상태를 비교하여 불일치하는 스택 Pod를 정리하는 작업(Cleanup)을 수행합니다.

Cleanup은 아래의 조건에 따라 수행됩니다.

- **스택 Pod 또는 매칭된 서비스가 존재하지 않는 경우** (DDB에는 존재하지만 쿠버네티스 클러스터에는 없는 경우, 또는 그 반대의 경우)
- **스택의 TTL(Time-To-Live)이 만료된 경우**

이처럼 Container Provisioner는 주기적으로 스케줄링되어 불필요한 리소스를 삭제하며 스택의 TTL을 포함한 라이프사이클을 관리합니다. 스택의 TTL은 기본값 2시간이며, 이는 환경 변수를 통해 변경할 수 있습니다.

스케줄링 간격은 기본값 10초로, 이 또한 환경 변수를 통해 변경할 수 있습니다. 과도하게 짧은 간격의 경우 그 만큼의 CPU/메모리 소모 및 쿠버네티스 API에 대한 많은 네트워크 접근이 발생할 수 있고, 너무 긴 간격의 경우 불필요한 워커 노드 리소스 소모와 UX에 영향을 미칠 수 있기 때문에 적절하게 판단하세요.

![scheduler](images/4-scheduler/image.png)

이 작업은 마치 쿠버네티스의 Controller Manager의 컨트롤 루프(Reconcile Loop)와 유사하게 동작하며, 컨트롤러가 API 서버를 거쳐 etcd와 상호작용하는 것 처럼
Container Provisioner는 양방향으로 DDB와 쿠버네티스 클러스터(정확히는 API 서버)와 상호작용합니다. 즉 Desired State와 Current State는 양측에 존재하며, Container Provisioner는 이를 일치시키기 위해 루프를 돌며 상태를 조정(Reconcile)합니다.
