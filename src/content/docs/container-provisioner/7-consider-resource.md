---
title: 7. 리소스/인스턴스 유형 선택 방법
sidebar:
    order: 7
---

문제(챌린지)를 등록할 때 스택(컨테이너 환경)을 제공할 경우 적절한 리소스 요청량 및 제한량을 설정하는 것이 가장 중요합니다.
너무 낮은 리소스 설정은 문제가 정상적으로 동작하지 않을 수 있으며, 너무 높은 리소스 설정은 불필요한 비용 증가와 리소스 낭비, 스케줄링 실패 등을 초래할 수 있습니다.

또한 CTF를 시작하기 전 문제들의 총 리소스 요구량과 참여자의 수, 참여자 당 제한할 총 스택의 수를 고려하여 적절한 워커 노드의 인스턴스 유형과 노드의 분산 개수를 결정하는 것이 중요합니다.

계산된 총 리소스 요구량에서 20% 정도의 여유 리소스를 추가적으로 고려해야 하며, 스택이 구동되는 워커 노드는 백엔드와 마이크로서비스가 구동되는 노드와 별도로 고려해야 합니다.

이 문서에서는 문제 유형에 따른 적절한 리소스 설정 방법과 워커 노드의 인스턴스 유형, RDS, ElastiCache 인스턴스 유형에 대한 선택 방법에 대해 다룹니다.

### 문제 유형에 따른 리소스 설정 방법

컨테이너 리소스는 vCPU를 Millicores(mCPU) 단위로, 메모리는 MiB 단위로 작성합니다. Guaranteed QoS를 위해 요청량과 제한량을 동일하게 설정하는 것을 권장합니다.

#### Web

리소스를 가장 많이 요구하는 문제 유형은 대부분 웹 문제입니다. 또한 스펙트럼이 가장 넓은 문제 유형으로, 간단한 정적 웹 페이지부터 복잡한 데이터베이스, 무거운 런타임을 포함한 이미지 등 다양한 바리에이션이 존재합니다.

아래는 일반적인 웹 문제 유형에 따른 권장 리소스 설정 예시입니다. 문제에 따라 다를 수 있으므로 참고용으로만 활용하시고, 문제를 제작한 개발자가 직접 테스트하여 적절한 리소스 설정을 결정하는 것을 권장합니다.

| 세부 유형                   | vCPU | Memory    |
| --------------------------- | ---- | --------- |
| 정적 웹                     | 50m  | 64Mi      |
| 경량 웹 서버                | 100m | 128Mi     |
| 웹 + 경량 DB                | 200m | 256Mi     |
| Node.js / PHP               | 200m | 256–384Mi |
| Java/Spring                 | 500m | 512Mi     |
| 이미지 처리(FFmpeg, PIL 등) | 500m | 512Mi-1Gi |

#### Binary Exploitation (Pwn)

| 세부 유형     | vCPU    | Memory |
| ------------- | ------- | ------ |
| 단일 바이너리 | 50–100m | 64Mi   |

Pwnable과 Reversing 유형의 문제는 일반적으로 낮은 리소스를 요구합니다만, ptrace 등의 도구를 직접 사용하는 경우 비교적 높은 리소스를 요구할 수 있습니다.
하지만 대부분 50m vCPU와 64Mi 메모리로도 충분히 구동 가능합니다.

또한 스레드나 프로세스를 다수 생성하는 fork를 사용하는 문제의 경우 nproc 제한을 반드시 설정하는 것을 권장합니다.

#### Reverse Engineering

| 세부 유형     | vCPU    | Memory |
| ------------- | ------- | ------ |
| 단일 바이너리 | 50–100m | 64Mi   |

Reversing 문제 유형도 Pwn과 유사하게 낮은 리소스를 요구합니다. 다만 마찬가지로 무거운 도구나 라이브러리,
복잡한 스레딩 구조 등을 포함하고 있다면 더욱 더 많은 리소스를 요구할 수 있습니다.

---

그 외의 문제 유형은 일반적으로 격리된 컨테이너 환경을 필요로 하지 않으므로 리소스 설정에서 배제하였습니다.
Forensics, Crypto, Misc 문제 유형은 소스코드 파일 업로드 기능을 이용하세요.

Pod(또는 컨테이너)는 한번 종료되면 리소스가 해제되고 복구되지 않으니 OOM 문제나 CPU 부족 문제로 인해 풀이자가 불편을 겪지 않도록 충분한 리소스를 할당하는 것이 중요합니다.

추가적으로 문제를 제작하면서 어느정도의 리소스가 필요한지 직접 테스트 해보는 것이 가장 좋겠지만, 그러지 못할 경우 아래의 LLM 프롬포트를 활용하여 리소스 설정을 예측할 수 있습니다.

```
이 프로젝트/소스코드/서비스는 CTF 문제로 제공될 예정이며, 유저 개개인에게 문제별로 격리된 컨테이너 환경에서 제공될 것입니다.
이때 컨테이너는 Kubernetes 환경에서 단일 Pod로 구동되며, Guaranteed QoS를 위해 컨테이너의 리소스 요청량과 제한량이 동일하게 설정될 것입니다.

때문에 빌드된 컨테이너 이미지가 구동되기 위한 적절한 리소스 요청량과 제한량을 vCPU(mCPU 단위)와 메모리(MiB 단위)를 예측해 주십시오.
주요 기능과 사용된 기술 스택, 예상되는 부하 등을 고려하여 가능한 정확한 수치를 제시해 하십시오.

여유를 위해 20% 정도의 추가 리소스를 포함하십시오. 또한 Peak 부하 상황을 고려하여 리소스 설정이 충분한지 평가해 주십시오.

<필요 시 추가 정보 작성>
```

### 백엔드 노드, 스택 워커 노드의 인스턴스 유형 선택

노드의 인스턴스 유형과 개수를 결정하기 위해선 전제 조건을 가정하여 총 리소스 요구량을 산출해야 합니다. 때문에 실제로 계산할땐 참여자의 수와 문제별 리소스 요구량, 그리고 각 참여자 별로 만들 수 있는 최대 스택 수 등을 고려해야 합니다.
전제 조건은 아래와 같습니다.

- 참여자 수: N명
- 참여자가 만들 수 있는 최대 스택 수: 3개
- 문제의 평균 리소스 요구량: 100m vCPU, 128Mi Memory
- 최악의 경우를 가정하여 모든 사용자가 최대 스택 수(3개)를 생성한다고 가정
- 전제적으로 20% 정도의 여유 리소스 포함

또한 노드의 수를 늘리냐, 인스턴스의 사양(유형)을 늘리냐에 따라 비용과 안정성, 확장성 측면에서 차이가 발생할 수 있으므로 적절한 균형점을 찾는 것이 중요합니다.

계산 공식은 아래와 같습니다.

- CTF 메인 서비스의 1 Replica 당 리소스 요구량은 300m vCPU와 512Mi Memory로 가정하며, Container Provisioner는 1 Replica 당 200m vCPU와 256Mi Memory를 요구한다고 가정합니다.
- Kubernetes에서 필요로하는 컴포넌트들은 백엔드 노드에 포함되어 있다고 가정하며, 800m vCPU와 1056Mi Memory를 추가로 요구한다고 가정합니다.

인스턴스는 `m7i-flex.large` 유형으로 가정합니다. 이는 2 vCPU와 8Gi Memory를 제공합니다. 이때 `m`, `Mi` 단위로 환산하며 여유 리소스 20%를 고려하면 아래와 같습니다.

```
CPU = 2 × 1000m × 0.8 = 1600m
Mem = 8192Mi × 0.8 ≈ 6550Mi
```

이는 곧 하나의 `m7i-flex.large` 인스턴스가 1600m vCPU와 6550Mi Memory를 제공할 수 있다는 의미이며, Replicas 수에 따라 요구량이 아래와 같이 산출됩니다.

```
Backend CPU =
  (replicas × 300m)
+ 200m (Provisioner)
+ 800m (k8s addons)

Backend Memory =
  (replicas × 512Mi)
+ 256Mi (Provisioner)
+ 1056Mi (k8s addons)
```

사용자의 수에 따라 Replicas 수는 아래와 같이 결정하는 것을 권장합니다.

|   Users | CTF 메인 replicas |
| ------: | ----------------: |
|  25-100 |                 2 |
| 125-250 |                 3 |
| 275-400 |                 4 |
| 425-500 |                 5 |

단, Container Provisioner는 높은 가용성을 요구하지 않고 단일로 운영되는 것을 권장하므로 Replicas 계산에서 포함하지 않았습니다.

---

다음으로 스택 워커 노드의 총 리소스 요구량에서 CPU와 Memory 여유는 각각 90%, 85%로 가정하여 산출합니다.
인스턴스 유형은 `c7i-flex.xlarge`(4 vCPU, 8Gi Memory)와 `c7i-flex.2xlarge`(8 vCPU, 16Gi Memory)로 가정하며, 각각 여유 리소스를 고려하면 아래와 같습니다.

```
c7i-flex.xlarge
CPU alloc = 4 × 1000m × 0.9 = 3600m
Mem alloc = 8192Mi × 0.85 ≈ 6963Mi

c7i-flex.2xlarge
CPU alloc = 8 × 1000m × 0.9 = 7200m
Mem alloc = 16384Mi × 0.85 ≈ 13926Mi
```

1명의 사용자가 최악의 경우 최대 3개의 스택을 생성한다고 가정하였을 때, 사용자 당 요구되는 리소스는 아래와 같습니다.

```
users_per_node_cpu = alloc_cpu / 360m
users_per_node_mem = alloc_mem / 461Mi

users_per_node = min(cpu 기준, mem 기준)
```

때문에 xlarge 인스턴스는 사용자 당 약 10개의 스택을 수용할 수 있으며, 2xlarge 인스턴스는 사용자 당 약 20개의 스택을 수용할 수 있습니다.
여태까지 계산된 공식은 마지막에 Python 코드로 작성해두었습니다. 필요 시 참고 용도로만 활용하세요.

이를 반영하여 사용자 수에 따른 인스턴스 유형과 노드 수, 총 리소스 요구량은 아래와 같습니다.

| Users | Backend Nodes | CTF Replicas | Stack Nodes (xlarge or 2xlarge) |
| ----: | ------------- | -----------: | ------------------------------: |
|    25 | 1             |            2 |                               3 |
|    50 | 1             |            2 |                               5 |
|    75 | 1             |            2 |                               8 |
|   100 | 1             |            2 |                              10 |
|   125 | 2             |            3 |                              13 |
|   150 | 2             |            3 |                              15 |
|   175 | 2             |            3 |                               9 |
|   200 | 2             |            3 |                              10 |
|   225 | 2             |            3 |                              12 |
|   250 | 2             |            3 |                              13 |
|   275 | 2             |            4 |                              14 |
|   300 | 2             |            4 |                              15 |
|   325 | 2             |            4 |                              17 |
|   350 | 2             |            4 |                              18 |
|   375 | 2             |            4 |                              19 |
|   400 | 2             |            4 |                              20 |
|   425 | 2             |            5 |                              22 |
|   450 | 2             |            5 |                              23 |
|   475 | 2             |            5 |                              24 |
|   500 | 2             |            5 |                              25 |

**주의: 이는 단순 참고용 예시이며, 실제로 요구되는 총 리소스의 양에 따라 노드 인스턴스 타입과 수, Replicas가 결정됩니다. 반드시 참가자들과 모든 문제에 대한 리소스를 바탕으로 직접 산출하여 결정하시기 바랍니다.**

### RDS, ElastiCache 인스턴스 유형 선택

RDS는 PostgreSQL, ElastiCache는 Redis를 권장하며 이를 기준으로 인스턴스 유형을 선택합니다. 최대 500명을 기준으로 생각하였을때 Replica나 Read Replica, Multi-AZ 구성은 필요하지 않다고 판단됩니다.
때문에 단일 인스턴스로 운영하도록 계산합니다.

**RDS**

| Users | Instance      | vCPU | RAM   |
| ----- | ------------- | ---- | ----- |
| ~50   | db.t4g.micro  | 2    | 1 GiB |
| ~100  | db.t4g.small  | 2    | 2 GiB |
| ~250  | db.t4g.medium | 2    | 4 GiB |
| ~500  | db.t4g.large  | 2    | 8 GiB |

ElastiCache의 경우 각 유저가 요구하는 최소 캐싱 용량을 1.5MiB로 가정합니다. 실제로는 이보다 훨씬 적은 용량을 요구하지만, 여유를 두기 위해 이 정도로 가정합니다.

```
memory_per_user = 1.5 × 1.3 = 1.95 MiB (30% 여유 포함)
```

| Users | Instance         | RAM      |
| ----- | ---------------- | -------- |
| ~50   | cache.t4g.micro  | 0.5 GiB  |
| ~150  | cache.t4g.small  | 1.37 GiB |
| ~300  | cache.t4g.medium | 3.22 GiB |
| ~500  | cache.t4g.large  | 6.38 GiB |

---

### 참고 및 주의사항

아래는 앞서 설명한 내용을 바탕으로 사용자 수에 따른 백엔드 노드 수, CTF 메인 서비스 Replicas 수, 스택 워커 노드 수와
RDS, ElastiCache 인스턴스 유형에 따른 표는 오로지 예시로, 참고용으로만 활용하시기 바랍니다.

**실제로는 각 참여자 수와 문제별 리소스 요구량, 그리고 각 참여자 별로 만들 수 있는 최대 스택 수 등을 고려하여 직접 산출해야 합니다. 항상 여유를 두고 계획하시기 바랍니다.**

---

```py
import math

USERS = list(range(25, 501, 25))

# Backend node
CTF_CPU = 300      # m
CTF_MEM = 512      # Mi
PROV_CPU = 200
PROV_MEM = 256
ADDON_CPU = 800
ADDON_MEM = 1056

BACKEND_NODE_CPU = 2000 * 0.8    # m7i-flex.large
BACKEND_NODE_MEM = 8192 * 0.8

def ctf_replicas(users):
    if users <= 100:
        return 2
    elif users <= 250:
        return 3
    elif users <= 400:
        return 4
    else:
        return 5

# Stack worker node
STACK_CPU_PER_USER = 360   # m (3 stacks + 20%)
STACK_MEM_PER_USER = 460.8 # Mi

STACK_NODES = {
    "xlarge": {
        "cpu": 4000 * 0.9,
        "mem": 8192 * 0.85,
        "users_per_node": 10
    },
    "2xlarge": {
        "cpu": 8000 * 0.9,
        "mem": 16384 * 0.85,
        "users_per_node": 20
    }
}

for users in USERS:
    # Backend
    replicas = ctf_replicas(users)
    backend_cpu = replicas * CTF_CPU + PROV_CPU + ADDON_CPU
    backend_mem = replicas * CTF_MEM + PROV_MEM + ADDON_MEM

    backend_nodes_cpu = math.ceil(backend_cpu / BACKEND_NODE_CPU)
    backend_nodes_mem = math.ceil(backend_mem / BACKEND_NODE_MEM)
    backend_nodes = max(backend_nodes_cpu, backend_nodes_mem)

    # Stack
    stack_cpu_total = users * STACK_CPU_PER_USER
    stack_mem_total = users * STACK_MEM_PER_USER

    node_type = "xlarge" if users <= 150 else "2xlarge"
    users_per_node = STACK_NODES[node_type]["users_per_node"]
    stack_nodes = math.ceil(users / users_per_node)

    print(
        f"{users} users | "
        f"Backend nodes: {backend_nodes}, "
        f"CTF replicas: {replicas} | "
        f"Stack nodes ({node_type}): {stack_nodes}"
    )
```
