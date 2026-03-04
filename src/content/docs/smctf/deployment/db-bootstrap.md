---
title: DB 및 부트스트랩
sidebar:
    order: 122
---

SMCTF는 PostgreSQL을 기본 데이터베이스로 사용하며, MySQL 등으로 대체할 수 있습니다. 다만 프로덕션 환경에선 로컬에서 PostgreSQL을 실행하는 것이 아닌 RDS와 같은 별도의 외부 데이터베이스 서비스를 사용하세요.

애플리케이션은 Stateless로 설계되었으며, SQLite와 같은 로컬 파일 기반 데이터베이스는 지원하지 않습니다.

DB ER(Entity Relationship)은 [nullforu/smctf/internal/models](https://github.com/nullforu/smctf/tree/main/internal/models) 레포지토리에서 확인할 수 있습니다.

### DB 부트스트랩

초기 관리자 부문(Admin), 팀(Admin), 그리고 초기 관리자 유저를 생성하기 위한 부트스트랩 기능을 제공합니다. 이는 아래의 [환경 변수](/smctf/deployment/envs)에서 설정할 수 있습니다.

```ini
# Bootstrap
BOOTSTRAP_ADMIN_TEAM=true
BOOTSTRAP_ADMIN_USER=true
BOOTSTRAP_ADMIN_USERNAME=admin
BOOTSTRAP_ADMIN_EMAIL=
BOOTSTRAP_ADMIN_PASSWORD=
```

이때 `BOOTSTRAP_ADMIN_TEAM`을 설정하면 자동으로 관리자 부문과 관리자 팀이 생성됩니다. 기본적으로 `Admin` 식별자로 생성되며 이는 변경할 수 없습니다. 
이는 프론트엔드에서 자동으로 숨겨지도록 처리됩니다. 

`BOOTSTRAP_ADMIN_USER`를 설정하면 초기 관리자 유저가 생성됩니다. 이때 `BOOTSTRAP_ADMIN_USERNAME`, `BOOTSTRAP_ADMIN_EMAIL`, `BOOTSTRAP_ADMIN_PASSWORD` 환경 변수를 통해 초기 관리자 계정의 사용자 이름, 이메일, 비밀번호를 설정할 수 있습니다.

이름, 이메일과 상관 없이 `admin` 역할을 가진 관리자 유저라면 일반유저에겐 자동으로 숨겨집니다. 자세한 내용은 [유저](/smctf/users) 문서를 참조하세요.
