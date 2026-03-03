---
title: 문제
sidebar:
    order: 70
---

문제(챌린지)는 참가자들이 풀이하는 단위입니다. 문제 목록 페이지에서 해당 문제에 대한 정보와 풀이 상태, [스코어링 시스템](/smctf/advanced/dynamic-score)에 의한 변동된 점수 등을 확인할 수 있습니다.

![Challs](/smctf/imgs/challs.png)

_기본적으로 카테고리별로 정렬되지만, 필요에 따라 정렬하지 않을 수도 있습니다._

![Challs Detail](/smctf/imgs/challs_modal.png)

문제의 상세 정보에선 더욱 세부적인 정보를 추가적으로 확인할 수 있으며 문제에서 제공할 경우 [문제 파일](/smctf/advanced/s3)이나 [스택](/smctf/advanced/stack) 정보를 확인할 수 있습니다.

![Challs Stack](/smctf/imgs/challs_stack.png)

_단, 위 두 정보는 문제 설정에 따라 제공되지 않을 수 있습니다._

### 선행 문제

![Challs Precede](/smctf/imgs/challs_previous.png)

문제에 선행 문제가 설정된 경우 해당 이전 문제를 풀이해야만 다음 문제를 풀이할 수 있습니다.
이전 문제를 풀이하기 전엔 해당 문제는 잠긴 상태가 되며 내용 확인 및 파일 다운로드, 스택 생성, 플래그 제출 등이 불가능합니다.

리벤지(Revenge) 문제나 시리즈가 있는 문제 등에서 이를 활용할 수 있습니다.

### 대회 시작 전 또는 종료 후

대회 운영자는 [사이트 설정](/smctf/admin/site-settings)에서 대회 시작 시각 또는 종료 시각을 설정할 수 있습니다. 대회 시작 전과 종료 후엔 아래와 같이 표시되며 각각에 맞는 제약이 적용됩니다.

**대회 시작 전**

- 문제 목록 조차 공개되지 않으며, 문제 풀이와 관련한 모든 기능이 제한됩니다.

![Challs Not Started](/smctf/imgs/challs_not_started.png)

**대회 종료 후**

- 문제 목록과 상세 정보, 파일 다운로드나 스코어보드 조회와 같은 일부 기능은 종료 후에도 여전히 이용할 수 있습니다.

![Challs Ended 2](/smctf/imgs/challs_ended_2.png)

- 하지만 플래그 제출과 스택 생성 등의 문제 풀이와 관련된 기능은 종료 후에 제한됩니다. 
- 스택도 대회 종료 후 운영자의 판단에 따라 자동으로 삭제될 수 있으니 주의하세요.

![Challs Ended](/smctf/imgs/challs_ended.png)

### 카테고리

문제는 아래와 같은 카테고리로 분류됩니다. 문제 생성 시 카테고리를 지정할 수 있습니다.

- Web
- Web3
- Pwnable
- Reversing
- Crypto
- Forensics
- Network
- Cloud
- Misc
- Programming
- Algorithms
- Math
- AI
- Blockchain

