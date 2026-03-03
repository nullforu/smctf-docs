---
title: 스코어보드
sidebar:
    order: 80
---

스코어보드는 CTF 플랫폼에 있어 가장 중요한 기능 중 하나입니다. 
SMCTF는 타입라인과 리더보드에 대한 스코어보드 기능을 제공하며, 기본적으로 팀 단위의 스코어보드를 제공하지만 옵션에 따라 유저 단위의 스코어보드도 제공합니다.

### 타임라인

타임라인은 상위 10개의 팀 또는 유저의 점수 변화를 시간에 따라 그래프를 통해 시각적으로 보여주는 기능입니다. 

![Scoreboard Timeline 1](/smctf/imgs/scoreboard_timeline_1.png)
![Scoreboard Timeline 2](/smctf/imgs/scoreboard_timeline_2.png)
![Scoreboard Timeline 3](/smctf/imgs/scoreboard_timeline_3.png)

_우측 상단의 Users | Teams 메뉴를 통해 팀 단위 또는 유저 단위의 타임라인을 선택할 수 있습니다._

![Scoreboard Timeline Teams](/smctf/imgs/scoreboard_timeline_teams.png)
![Scoreboard Timeline Users](/smctf/imgs/scoreboard_timeline_users.png)

### 리더보드

리더보드는 모든 팀 또는 유저들에 대해 순위와 스코어, 풀이 정보 및 First Blood 여부 등을 표시해주는 기능입니다. 

![Scoreboard Leaderboard](/smctf/imgs/scoreboard_leaderboard.png)

### 실시간 업데이트

SMCTF는 SSE를 기반으로 스코어보드 실시간 업데이트 기능을 제공합니다. 이를 통해 플래그 제출 등의 스코어보드 변동이 생긴다면 자동으로 타임라인과 리더보드가 업데이트되어 최신 상태를 유지할 수 있습니다.

![Scoreboard Realtime](/smctf/imgs/scoreboard_realtime.png)

필요시 마찬가지로 우측상단의 Live On/Off를 통해 이를 켜거나 끌 수 있습니다. 이에 대한 자세한 내용은 아래의 기술 블로그를 참조하세요.

- https://articles.swua.kr/development/2026-02-27-development-mitigating-thundering-herd-with-redis
