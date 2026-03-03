---
title: 개요
sidebar:
    order: 10
---

**SMCTF**는 세명컴퓨터고등학교의 DevOps 및 클라우드 컴퓨팅 동아리인 [Null4U](https://github.com/nullforu)에서 개발된 CTF 플랫폼입니다.

![preview](/smctf/imgs/home.png)

![preview](/smctf/imgs/ui_theme_dark_2.png)

쉬운 사용성과 유연한 배포, 그리고 기본적으로 제공되는 문제별 컨테이너 기반의 격리된 환경을 특징으로 하는 CTF 플랫폼으로, 누구나 MIT License를 기반으로 자유롭게 사용하고 기여할 수 있습니다.

_(기여시 가이드라인을 참조해주세요.)_

### 프로젝트 배경

기존의 CTF 플랫폼을 사용하여 [SCA](https://www.instagram.com/smc.sec_sca)와 같은 해킹/보안 동아리에서 CTF 대회를 개최하는데 있어 아래와 같은 문제점이 있었고, 실제로 이로 인해 대회 운영에 차질이 있었기도 했습니다.

- 기존 오픈소스 CTF 플랫폼을 사용하기 위해선 이에 따른 학습이 필요하였으며, 불필요한 기능 또한 포함되어 있어 러닝 커브가 있었음.
- 각 문제에 대한 개별적인 컨테이너 환경 또는 인스턴스/VM 환경을 제공하기가 어려웠으며, 검증되지 않은 외부 플러그인을 통한 솔루션은 신뢰되지 않았음.
- DB와 프론트엔드를 포함한 전체적인 시스템이 단일 Docker 컨테이너 이미지로 제공되었기 때문에 유연한 배포가 어렵고, 이에 따른 인스턴스 부하가 발생하였음.
- 상세한 로깅이나 모니터링과 같은 Observability 기능이 부족하여 대회 운영에 어려움이 있었음.

이러한 이유로 세명컴퓨터고등학교에서 자체적인 CTF 플랫폼을 기획하였고, 교외에서도 사용할 수 있도록 MIT License 아래에서 오픈소스로 공개하였습니다.

기획된 새로운 플랫폼은 쉬운 사용성과 유연한 배포, 그리고 문제별 격리된 환경을 기본적으로 제공하며 대회 운영에 필요한 인프라 배포를 위한 Terraform 코드나 보고계신 문서가 자세히 제공됩니다.

---

> SMCTF는 세명컴퓨터고등학교의 약칭인 SMC와 CTF의 합성어로, SMCTF라는 이름은 세명컴퓨터고등학교에서 개발된 CTF 플랫폼이라는 의미를 담고 있습니다.
>
> 또한 프로젝트 구조의 smctfe는 SMCTF와 Frontend(FE)의 합성어로, SMCTF의 프론트엔드 부분을 담당하는 레포지토리입니다. 각 레포지토리는 역할에 따라 독립적으로 유지보수됩니다.
>
> - **Backend**: [nullforu/smctf](https://github.com/nullforu/smctf)
> - **Frontend**: [nullforu/smctfe](https://github.com/nullforu/smctfe)
> - **Container Provisioner**: [nullforu/smctf-provisioner](https://github.com/nullforu/smctf-provisioner)
> - **Infra**: [nullforu/smctf-infra](https://github.com/nullforu/smctf-infra)
> - **Docs**: [nullforu/smctf-docs](https://github.com/nullforu/smctf-docs)
>
> 여기서 Container Provisioner는 각 문제에 대한 독립적인 컨테이너 환경(스택)을 제공하는 마이크로서비스로, [Container Provisioner](/container-provisioner) 문서에서 자세히 설명합니다.

각 기능들에 대해선 다음 페이지부터 자세히 설명합니다. 언급되지 않은 부분이 있을 수 있으니, 이러한 부분에 대해선 Docs 레포지토리에 PR 또는 이슈로 남겨주시면 감사드리겠습니다.

### Tech Stack

프로젝트는 다음과 같은 기술로 구현되었습니다.

- Backend: [Go](https://go.dev/), [Gin](https://github.com/gin-gonic/gin), [Bun ORM](https://bun.uptrace.dev/)
- Container Provisioner: [Go (nullforu/container-provisioner-k8s)](https://github.com/nullforu/container-provisioner-k8s)
- Frontend: [React (nullforu/smctfe)](https://github.com/nullforu/smctfe)
- Database, Cache: [PostgreSQL](https://www.postgresql.org/)(instead of MySQL/MariaDB), [Redis](https://redis.io/)
- Testing: [Testcontainers for Go](https://github.com/testcontainers/testcontainers-go)
- Infra, CI/CD (TBD): AWS, EKS, Terraform, Cloudflare, GitHub Actions, etc.

---

![AWS Architecture](/smctf/imgs/architecture_aws.png)

![Kubernetes Architecture](/smctf/imgs/architecture_k8s.png)

<!--
- Overview (+Home) - 소개, 주요 기능, 아키텍처 개요, 기술 스택, 라이선스 등등 + 홈 화면 UI : 10
    = CTF 홈 사진, 인프라 사진 x2
- AuthN/AuthZ - 가입 키, 가입, 로그인, 토큰 관리 등등 : 20
    = 헤더 사진 + 홈 화면 로그인, 로그인시 이용 가능 사진, 가입 사진, 인증키 사진(관리자), 로그인 사진
- Divisions - 대회 부문(트랙, 디비전) 설명 : 30
    = 대회 부문 관련 사진(탭) + 관리자 
- Teams - 팀 기능 소개 : 40
    = 팀 목록 사진, 팀 페이지 사진
- Users, RBAC - 유저, RBAC, 차단/제한, 관리자 유저 등등 : 50
    = 유저 목록 사진, 유저 페이지 사진, 유저/관리자 역할 사진, 차단/제한 사진
    - Profile - 유저 프로필 및 내 프로필 등등 : 60 (통합)
        = 유저 프로필 사진, 내 프로필 사진 (길면 두쪽으로 나눠서)
- Challs - 문제 페이지, 풀이 등등 : 70
    = 문제 목록 사진, 문제 상세 사진, CTF 시작/종료 사진
- Scoreboard - 스코어보드, 리더보드, 타임라인, 실시간 등등 : 80
    = 타임라인 사진(3개), 리더보드 사진
- Theme - UI 테마 + i18n 지원 등등 : 90
    = 화이트/다크 테마 사진, i18n 사진
- Admin : 100
    - Challenge Management - 문제 등록, 수정 등등 관리 : 101
        = 문제 등록(2개)/수정 사진(3개)
    - Division Management - 대회 부문(트랙, 디비전) 관리 : 102
        = 대회 부문 관리 사진(생성)
    - User Management - 유저 관리 (팀 이동, 차단/제한 등등) : 103
        = 유저 관리 사진(팀 이동, 차단/제한)
    - Team Management - 팀 관리 (팀 생성 등등) : 104
        = 팀 관리 사진(생성)
    - Stack Management - 스택 관리 (삭제 등등) : 105
        = 팀 관리 사진(삭제)
    - Registration Key Management - 가입 키 관리 : 106
        = 가입 키 관리 사진(생성, 목록)
    - Site Settings - 사이트 설정 (대회 기간, UI 커스텀 등) : 107
        = 사이트 설정 사진(대회 기간, UI 커스텀)
    - Reports : 108
        = 보고서 사진 YAML/JSON

- Advanced Features : 110
    - stack - 스택에 대해서 : 111
        = 문제 내 스택 사진, 429 + 3 limit
    - s3 - 문제 파일 저장소로서의 S3 : 112
        = 문제 파일 사진 + AWS 사진 + Presigned URL 사진
    - dynamic score - Dynamic Scoring 시스템 : 113
    - rate limit - 적용되는 리미트들 : 114
    - loggings - 로깅 시스템과 OpenMetrics : 115

- Deployment and Development : 120
    - envs - 환경 변수 설명 : 121
    - bootstrap - 실행시 자동으로 필요한 리소스들을 생성하는 부트스트랩 기능 설명 : 122
    - caching - 캐싱 관련해서 시스템 설명 : 123
    - db - DB ER 및 마이그레이션 설명 : 124
    - dummy - 더미 데이터 생성 스크립트 설명 : 125
    - yaml2sql - YAML2SQL 스크립트 설명 : 126
    - testing - 테스트 등등 : 127

- A. API Reference : 1010
- B. Performance : 1020
- C. Security : 1030
- D. ToS, Privacy Policy : 1040

-->
