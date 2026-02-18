---
title: 18. Redis 캐싱
sidebar:
    order: 110
---

SMCTF에서 Redis는 크게 캐싱 레이어와 [Rate Limiting](./16-rate-limit.md) 레이어로 사용됩니다. 이 문서에서는 캐싱 레이어에 대해 설명합니다.

다음과 같은 기능과 설정 등을 캐싱 레이어에서 지원합니다.

- JWT Refresh 토큰 정보 (`refresh:<UUID>`)
- App Config (사이트 설정) DB 쿼리 결과 (`app_config:cached`)
- Timeline 및 Leaderboard DB 쿼리 결과 (`timeline:users`, `timeline:teams`, `leaderboard:users`, `leaderboard:teams`)

강제로 캐싱을 무효화하려면 아래의 명령어를 통해 Redis에서 해당 키를 삭제할 수 있습니다.

```bash
redis-cli --scan --pattern "pattern:*" | xargs redis-cli UNLINK
```

이때 외부 Redis 엔드포인트를 별도로 지정해야 할 수 있습니다. 이 경우 `-h`, `-p` 플래그를 사용하여 Redis 호스트를 지정하세요.

```bash
export REDIS_HOST=example.com
export REDIS_PORT=6379
redis-cli -h $REDIS_HOST -p $REDIS_PORT --scan --pattern "pattern:*" | xargs redis-cli -h $REDIS_HOST -p $REDIS_PORT UNLINK
```
