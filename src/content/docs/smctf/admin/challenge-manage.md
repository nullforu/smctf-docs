---
title: 문제 관리
sidebar:
    order: 101
---

### 문제 생성

문제를 생성하기 위해선 아래와 같은 필수적인 정보들이 필요합니다. 

- 문제 제목(마크다운 지원), 문제 설명, 카테고리([참고](/smctf/challs#카테고리))
- 기본(초기) 점수, 최저 점수([참고](/smctf/advanced/dynamic-score))
- 플래그(수정시 새로 입력해야하며 Bcrypt 해시로 저장됩니다.)
- 활성화 여부(비활성화된 문제는 참가자들이 풀이할 수 없습니다.)

![Create Challs 1](/smctf/imgs/admin_challs_create_1.png)

또한 아래와 같은 선택적인 정보들도 입력할 수 있습니다.

- 이전(선행) 문제([참고](/smctf/challs#선행-문제))
- 챌린지 파일([참고](/smctf/advanced/s3))
- 스택 정보([참고](/smctf/advanced/stack))

![Challs File](/smctf/imgs/admin_challs_file.png)

_챌린지 파일은 ZIP 형태로 업로드해야 하며, 업로드된 파일은 S3 스토리지에 저장되고 Presigned URL 형태로 참가자들에게 제공됩니다. 자세한 내용은 [챌린지 파일](/smctf/advanced/s3) 문서를 참조하세요._

![Create Challs Stack](/smctf/imgs/admin_challs_stack.png)

_스택 정보에서 노출 포트는 TCP/UDP 중 1-65535 사이의 정수여야 하며 최대 24개까지 설정할 수 있습니다._

![Create Challs Port](/smctf/imgs/admin_challs_port.png)

_자세한 내용은 [스택](/smctf/advanced/stack) 문서를 참조하세요._

### 문제 관리

생성된 문제는 문제 관리 탭에서 수정하거나 삭제할 수 있습니다. **삭제 시 해당 문제에 대한 모든 풀이 기록과 관련 정보가 함께 삭제되며, 복구할 수 없으니 주의하세요.**

![Manage Challs](/smctf/imgs/admin_challs.png)

_Edit 버튼을 클릭하여 문제에 대한 설정 항목을 개별적으로 수정할 수 있습니다._

![Manage Challs Edit](/smctf/imgs/admin_challs_edit.png)

_플래그 수정 시 기존 플래그는 보이지 않으며 유효하지 않게 됩니다. 새로운 플래그를 입력해야 하며, 입력된 플래그는 마찬가지로 Bcrypt 해시로 저장됩니다._

![Manage Challs Flag](/smctf/imgs/admin_challs_flag.png)
