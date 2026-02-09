---
title: 6. NetworkPolicy 구성
---

Container Provisioner, 메인 CTF 서비스와 스택 Pod들은 동일한 Kubernetes 클러스터에서 동작합니다. 따라서 스택 Pod들이 메인 CTF 서비스나 Container Provisioner 마이크로서비스에 접근할 수 없도록 Kubernetes NetworkPolicy를 구성해야 합니다.

이에 대한 예시는 아래와 같습니다. 
AWS EKS의 VPC CNI 플러그인을 기준으로 작성되었으며, 다른 CNI 플러그인을 사용하는 경우 다를 수 있습니다. EKS에서 NetworkPolicy를 활성화하는 방법에 대해서는 [공식 문서](https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html)를 참고하세요.

(프로젝트에서 제공되는 Terraform 인프라를 통해 배포할 경우 자동으로 NetworkPolicy 옵션을 활성화하므로 별도의 설정이 필요하지 않습니다.)

```yaml
# Enable NetworkPolicy in AWS VPC CNI settings. ref: https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html
# This NetworkPolicy is based on VPC CNI in AWS EKS cluster. other CNI plugins may require different configurations.

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-ingress-to-backend
  namespace: backend
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchExpressions:
              - key: kubernetes.io/metadata.name
                operator: NotIn
                values:
                  - stacks
```

마이크로서비스는 실행 시 모든 네임스페이스에 대해 최소 하나의 NetworkPolicy 존재 여부를 확인합니다. 그 이유는 앞서 설명한 내용과 같습니다.

## 스택 Pod 간 네트워크 격리

이 부분에 대해선 개발 팀에서 많은 고민을 했습니다. 
결론적으로 스택 Pod 간 네트워크 격리는 기본적으로 제공하지 않기로 결정하였고, Native Kubernetes에선 Pod 간 네트워크 격리를 구현하기가 현실적으론 불가능하다고 판단하였습니다.

이에 대한 자세한 내용은 아래의 레포지토리 이슈를 참고하세요.

- Refs: https://github.com/nullforu/container-provisioner-k8s/issues/6

NetworkPolicy를 사용하지 않고 initContainers를 통해 iptables 규칙을 적용하는 방법도 고려했으나, 이는 보안상의 취약점과 Kubernetes 네트워킹 모델과 충돌이 발생한다고 판단하였습니다.

또한 스택 Pod 간 네트워크 격리를 하지 않아도 CTF 운영상 큰 문제가 없다고 판단하였습니다. 스택 Pod는 언제든지 재생성될 수 있으며, 플래그 제출이 완료된다면 즉시 삭제되는 원칙으로 운영되기 때문입니다.

추가적으로 Container Provisioner는 별도의 인증 및 권한 관리 없이 REST API가 호출될 수 있기 때문에 퍼블릭 네트워크에 노출되지 않도록 주의해야 하지만, 
디버깅의 이유로 [대시보드](./5-dashboard.md) 등을 AWS ALB 등으로 노출해야하는 경우가 있을 수 있습니다. 

이땐 스택 Pod에서 NodePort를 통해 우회하여 접속할 수 있는 시나리오가 발생할 수 있기 때문에 NodePort가 겹치지 않도록 아래와 같은 NodePort 범위를 기본값으로 설정하였습니다.

- Backend NodePort: 30000-31000
- Stack NodePort: 31001-32767 (이 범위를 퍼블릭 워커 노드에서 `0.0.0.0/0`으로 접근을 허용)

이 범위는 환경 변수를 통해 변경할 수 있습니다. 마찬가지로 프로젝트에서 제공되는 인프라에선 기본적으로 관련 설정이 적용되어 있습니다.

---

2차적인 방어 수단으로 Container Provisioner 마이크로서비스의 HTTP REST API를 호출할 때 헤더에서 `X-API-KEY` 값을 요구하도록 설정할 계획입니다.
API Key는 환경변수로 주입되며, 메인 CTF 서비스에서 Container Provisioner API를 호출할 때 반드시 해당 헤더와 환경 변수로 설정된 값을 포함해야 합니다.

이 기능은 추후 제공될 예정입니다.
