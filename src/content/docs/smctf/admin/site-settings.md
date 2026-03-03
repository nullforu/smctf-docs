---
title: 사이트 설정
sidebar:
    order: 107
---

사이트 설정 탭에선 대회 시작 시간과 종료 시간, 홈 페이지의 제목과 설명, 그리고 헤더의 아이콘 옆 텍스트를 설정할 수 있습니다.

여기서 프론트엔드에 대한 모든 디자인, UX/UI 요소를 커스터마이징 할 순 없으며, 이를 원한다면 [프론트엔드 레포지토리](https://github.com/nullforu/smctfe)를 포크하거나 클론하여 직접 수정해야 합니다.

![Custom 1](/smctf/imgs/admin_custom_1.png)

이 페이지에서 수정 가능한 요소는 다음과 같습니다.

- 헤더 제목 및 설명
- 홈 페이지 제목 및 설명(마크다운 지원)
- 대회 시작 시간과 종료 시간

![Custom Header](/smctf/imgs/admin_custom_header.png)

![Custom 2](/smctf/imgs/admin_custom_2.png)
![Custom Home 1](/smctf/imgs/admin_custom_home_1.png)
![Custom Home 2](/smctf/imgs/admin_custom_home_2.png)

### 대회 시작 및 종료 시간

이에 대한 자세한 설명은 [문제](/smctf/challs#대회-시작-전-또는-종료-후) 문서를 참조하세요. 

![Custom Start End 1](/smctf/imgs/admin_custom_start_end.png)
![Custom Start End 2](/smctf/imgs/admin_custom_start_end_2.png)

대회 시작 시간 및 종료 시간은 RFC 3339 형식으로 입력해야 하지만, 편의를 위해 아래와 같이 입력할 수 있습니다.

서버는 UTC 시간대를 사용하므로 대한민국 시간대인 UTC+9 기준으로 입력해야 합니다. 위 입력에선 자동으로 `UTC +09:00` 시간대로 서버로 전송됩니다.

`Clear time` 버튼을 통해 시작 시간 또는 종료 시간에 대한 제한을 제거할 수 있으며, 두 값은 서로 독립적으로 설정됩니다.
