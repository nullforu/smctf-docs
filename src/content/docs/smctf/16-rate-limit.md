---
title: 16. 요청 속도 제한 설정
sidebar:
    order: 101
---

SMCTF는 Brute Force 공격 방지와 서비스의 안정성을 위해 일부 API 엔드포인트에 대한 기본적인 요청 속도 제한(Rate Limiting)을 구현하고 있습니다. 

다음은 요청 속도 제한이 적용되는 기능과 기본 설정 값입니다. 모두 [환경 변수](/smctf/14-envs-cors)에서 구성할 수 있습니다.

- 플래그 제출: `SUBMIT_WINDOW=1m`, `SUBMIT_MAX=10` (1분당 최대 10회 요청 허용)
- 스택 생성: `STACKS_CREATE_WINDOW=1m`, `STACKS_CREATE_MAX=1` (1분당 최대 1회 요청 허용 + 사용자당 최대 3개=`STACKS_MAX_PER_USER` 스택 생성 허용)

각각의 설정은 필요에 따라 조정할 수 있으며, 서비스의 특성과 예상되는 트래픽 패턴에 맞게 적절한 값을 선택하는 것이 중요합니다. 
너무 낮은 값으로 설정하면 정상적인 사용자가 불편을 겪을 수 있고, 너무 높은 값으로 설정하면 리소스가 과도하게 사용될 수 있으므로 주의해서 설정하세요.

이들은 모두 Redis를 통해 구현된 Rate Limiting으로, 전체적인 L7 HTTP/HTTPS 트래픽에 대한 Rate Limiting이 필요한 경우에는 별도의 API Gateway나 WAF 솔루션 또는 Nginx, Cloudflare와 같은 리버스 프록시를 구성하세요.
