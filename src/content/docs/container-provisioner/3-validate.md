---
title: 3. YAML Spec 검증 및 보안 솔루션
---

Container Provisioner는 스택 생성 요청 시, 운영자의 휴먼 에러나 적절하지 않은 요청으로 부터 호스트를 보호하기 위해 다양한 검증과 보안 솔루션을 강제로 적용합니다.

- 매니페스트는 공백이나 빈 문자열을 허용하지 않으며, 표준 YAML 형식만 허용합니다.
- 기본적인 필드 검증 및 Pod 단일 오브젝트만 허용합니다. (`kind: Pod` 및 `apiVersion: v1` 만 허용)
- targetPort는 반드시 1-65535 사이의 정수여야 하며, 컨테이너 포트 중 반드시 하나와 매칭되어야 합니다.
- 그 외의 검증에 대한 내용은 [internal/stack/validator.go](https://github.com/nullforu/container-provisioner-k8s/blob/main/internal/stack/validator.go) 소스코드를 참조하세요.

또한 아래의 보안 솔루션이 기본적으로 적용됩니다. 이는 강제로 적용되며, 변경할 수 없습니다.

- Pod 또는 컨테이너 보안 정책 제한을 위해 아래의 필드들은 직접 구성할 수 없으며, YAML 매니페스트에 포함될 경우 에러를 반환합니다.
    - `hostNetwork`, `hostPID`, `hostIPC`, `serviceAccountName`, `deprecatedServiceAccount`, `serviceAccountToken`, `nodeName`, `runtimeClassName`, `ephemeralContainers`, `hostPath`, `securityContext`
- 또한 아래의 필드들은 명시된 값으로 강제로 덮어씌워집니다.
    - `restartPolicy: Never`
    - `automountServiceAccountToken: false`
    - `enableServiceLinks: false`
    - `securityContext.seccompProfile.type: RuntimeDefault`
    - `privileged: false`
    - `allowPrivilegeEscalation: false` 등등. 

이는 곧 컨테이너 격리 및 호스트 워커 노드를 보호하기 위한 최소한의 보안 조치로, 스택 Pod는 절대로 특권을 가질 수 없습니다. (non-privileged)

또한 스택 Pod는 CTF 참여자의 페이로드에 따라 언제든지 종료되거나 OOM 등의 문제가 발생할 수 있습니다.

하지만 모든 문제(챌린지)는 동일한 환경에서 의도된 페이로드로 검증이 완료되었고, 때문에 이는 의도된 동작이므로 이에 대한 책임은 참여자 본인에게 있습니다.

**또한 최소한의 보안 조치가 적용되었음에도 불구하고, 참여자가 어떠한 방법으로든 호스트 워커 노드에 영향을 미치거나 다른 스택 Pod에 영향을 미치는 행위가 발생할 경우 이는 부정 행위 및 운영 방해로 간주되며, 즉시 퇴출되거나 적절한 제재가 가해질 수 있습니다.**

## OPA Gatekeeper 사용하기

앞서 언급한 기본적인 검증은 Container Provisioner 마이크로서비스에서 자체적으로 수행되는 1차적인 보안 조치이지만, 보다 세부적이고 Shift Left/Right 모두를 포함한 PaC(Policy as Code) 솔루션을 적용하고자 한다면 OPA Gatekeeper 또는 Kyverno와 같은 정책 엔진을 쿠버네티스 클러스터에 도입할 수 있습니다.

- 참고: https://articles.swua.kr/kubernetes/2026-01-13-kubernetes-pac-with-gatekeeper-and-kyverno

Gatekeeper의 Rego를 포함한 ConstraintTemplate 및 Constraint 리소스를 제공하진 않습니다. 필요 시 직접 작성하여 사용하시기 바랍니다.
