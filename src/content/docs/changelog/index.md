---
title: SMCTF Changelog
sidebar:
    order: 1
---

### v1.3.0 (2026-03-01)

아래와 같은 개선 및 기능이 추가되었습니다. 기존 버전과 호환되지 않는 변경 사항이 포함되어 있으며, [Container Provisioner 1.2.0](/changelog/container-provisioner) 이상과 호환됩니다. [Infrastructure v1.0.0](/changelog/infra)는 그대로 호환됩니다.

---

- 문제 풀이에 대한 사전 요구 조건(Prerequisite Challenge) 기능이 추가되었습니다. 특정 문제를 풀기 위해 먼저 풀어야 하는 문제를 설정할 수 있습니다. [#41](https://github.com/nullforu/smctf/pull/41)
- 하나의 스택에서 다수의 컨테이너 포트 및 UDP 프로토콜을 지원합니다. 이에 따라 관련 API의 요청 및 응답 DTO가 변경되었습니다. [#42](https://github.com/nullforu/smctf/pull/42)
- 실시간 리더보드 기능을 위한 SSE 핸들러가 추가되었으며, 이에 대한 스코어보드 계산과 관련한 내부 아키텍처가 수정되었습니다. [#43](https://github.com/nullforu/smctf/pull/43)
- HMAC 기반의 플래그 검증 로직이 Bcrypt 해싱으로 대체되었습니다. 이에 따라 플래그 저장 방식과 검증 로직이 변경되었습니다. [#45](https://github.com/nullforu/smctf/pull/45)
- 대회 트랙(디비전) 기능이 추가되었습니다. 이제 학생부, 일반부와 같이 전형(Track, 또는 Division)을 구분할 수 있습니다. [#46](https://github.com/nullforu/smctf/pull/46)

---

이는 프론트엔드 UI에도 영향을 미치는 업데이트로, 관련된 프론트엔드 업데이트가 함께 이루어졌습니다. [프론트엔드 v1.1.0](/changelog/frontend) 릴리즈를 참조하세요.

대규모 업데이트 및 내부 아키텍처 변경, DB 스키마(모델) 등이 다수 포함된 릴리즈로 이에 따른 문서를 새롭게 개편하였습니다. 이전 내용은 [Github 레포지토리](https://github.com/nullforu/smctf-docs)의 `deprecated-smctf`에서 확인할 수 있습니다.

### v1.2.0 (2026-02-22)

아래와 같은 개선 및 기능이 추가되었습니다. `v1.1.0`과 호환되며 [Container Provisioner v1.1.0](/changelog/container-provisioner), [Infrastructure v1.0.0](/changelog/infra)과 호환됩니다.

---

- JSON으로 구조화된 로깅을 지원하며 OpenMetrics 엔드포인트(`/metrics`)가 추가되었습니다. 이에 따라 로깅 및 모니터링 시스템이 크게 변경되었으며 더 이상 Discord/Slack 웹훅 로깅을 지원하지 않습니다. 이는 보안상의 이유도 있다고 판단하였기 때문에 이전 버전과 호환되지 않는 변경 사항입니다.
- 자세한 내용은 인프라 문서의 [로깅 및 모니터링](/infra/observability) 문서를 참조하세요. PR [#39](https://github.com/nullforu/smctf/pull/39)

---

- Admin 팀 및 초기 관리자 생성 기능이 추가되었습니다. 활성화 시 자동 DB 마이그레이션과 함께 Admin 팀과 초기 관리자 계정이 생성되는 기능으로, DB에 아무 데이터가 없는 상태에서만 실행됩니다.
- 자세한 내용은 [DB ER 및 마이그레이션](/smctf/deployment/db) 문서를 참조하세요. PR [#40](https://github.com/nullforu/smctf/pull/40)

---

- 이제 관리자 유저(Role=admin) 또한 집계에서 제외됩니다. 이에 대한 로직은 제한(차단)된 유저와 동일하게 처리됩니다.

### v1.1.0 (2026-02-18)

`v1.0.0` 릴리즈 이후 몇가지 개선과 기능 추가, 버그 수정을 포함한 릴리즈입니다. `v1.0.0`과 호환되지 않는 API 변경이 포함되어 있습니다.

---

- 가입 키(Registration Key)가 6자리 숫자가 아닌 16자리의 랜덤한 문자열로 변경되었으며, 일회성이 아닌 다회용으로 사용할 수 있도록 최대 사용 횟수 기능이 추가되었습니다.
- 자세한 내용은 업데이트된 [가입 인증 키 관리](/smctf/admin/registration-key-manage) 문서를 참조하세요. PR [#32](https://github.com/nullforu/smctf/pull/32)

---

- 유저에 대한 팀 이동 기능이 추가되었습니다. 관리자 페이지에서 특정 유저의 팀을 변경할 수 있습니다.
- 유저에 대한 제한(차단) 및 제한 해제 기능이 추가되었습니다. 차단된 유저는 문제 풀이가 불가하고 스코어보드에 반영되지 않습니다.
- 자세한 내용은 업데이트된 [유저](/smctf/users) 및 [유저 관리](/smctf/admin/user-manage) 문서를 참조하세요. PR [#33](https://github.com/nullforu/smctf/pull/33)

---

- 관리자는 모든 스택을 조회하고 직접 삭제할 수 있습니다.
- 자세한 내용은 업데이트된 [스택 관리](/smctf/admin/stack-manage) 문서를 참조하세요. PR [#36](https://github.com/nullforu/smctf/pull/36)

---

- 관리자는 대회 보고서(리포트)를 생성할 수 있습니다. 이는 JSON 또는 YAML 형태로 제공되며, 추후 PDF 형태로도 제공될 예정입니다.
- 자세한 내용은 업데이트된 [대회 보고서(리포트)](/smctf/admin/reports) 문서를 참조하세요. PR [#37](https://github.com/nullforu/smctf/pull/37)

---

이에 따른 관련된 프론트엔드 UI 수정 또는 개선이 이루어졌습니다.

- 문제 목록(`/challenges`) 페이지에서 카테고리별 그룹화 기능이 추가되었습니다.
- 일부 편집 가능한 항목에서 [Monaco Editor](https://microsoft.github.io/monaco-editor/)를 도입하였습니다.
- 관리자 페이지의 UI/UX가 개선되었으며 유저 관리, 스택 관리 및 보고서 생성과 관련된 탭이 추가되었습니다.

프론트엔드([nullforu/smctfe](https://github.com/nullforu/smctfe))는 백엔드와 별도의 저장소에서 관리되며 별도의 버전 릴리즈가 이루어집니다.
때문에 위 내용은 백엔드의 공식 릴리즈엔 포함되지 않지만 관련된 프론트엔드 업데이트임에 따라 함께 언급합니다.

---

그 밖에 아래와 같이 리펙토링이 이루어졌습니다. 자세한 내용은 각 PR 내용을 참조하세요.

- Normalize app config/challenge update API semantics and expand test coverage. [#35](https://github.com/nullforu/smctf/pull/35)
- Refactoring before v1.1.0 release. PR [#38](https://github.com/nullforu/smctf/pull/38)

### v1.0.0 (2026-02-15) (Pre Release)

SMCTF의 첫번째 공식 릴리즈로, Pre Release로 배포되었습니다.
`v1.1.0` 이후 추가된 기능을 제외한 모든 기능이 포함되어 있으며, 몇몇 API가 `v1.1.0` 이상과 호환되지 않을 수 있습니다.

```md
- chore(deps): bump esbuild, @sveltejs/vite-plugin-svelte and vite in /frontend by @dependabot[bot] in https://github.com/nullforu/smctf/pull/2
- chore(deps): bump github.com/quic-go/quic-go from 0.54.0 to 0.57.0 by @dependabot[bot] in https://github.com/nullforu/smctf/pull/1
- Add unit test and/or integration test coverage by @yulmwu in https://github.com/nullforu/smctf/pull/5
- fix: codecov comment behavior to default by @yulmwu in https://github.com/nullforu/smctf/pull/7
- Add db, repo and config package unit test coverage by @yulmwu in https://github.com/nullforu/smctf/pull/8
- Add file logging and Discord/Slack webhook logging by @yulmwu in https://github.com/nullforu/smctf/pull/10
- Add group/organization features by @yulmwu in https://github.com/nullforu/smctf/pull/12
- Added README preview images and chore script and frontend by @yulmwu in https://github.com/nullforu/smctf/pull/13
- Add team features by @yulmwu in https://github.com/nullforu/smctf/pull/15
- Add dynamic scoring feature by @yulmwu in https://github.com/nullforu/smctf/pull/16
- Chore/update dummy sql generator scripts by @yulmwu in https://github.com/nullforu/smctf/pull/17
- Add UI customization features by @yulmwu in https://github.com/nullforu/smctf/pull/19
- Add challenge file upload/download via AWS presigned url by @yulmwu in https://github.com/nullforu/smctf/pull/21
- Remove the "not affiliated with any team" feature for users. by @yulmwu in https://github.com/nullforu/smctf/pull/23
- Leaderboard improvements and First Blood feature addition by @yulmwu in https://github.com/nullforu/smctf/pull/24
- Implement Stack Instance in the SMCTF service using the Container Provisioner microservice by @yulmwu in https://github.com/nullforu/smctf/pull/25
- Improve and optimize frontend UI/UX and add internationalization by @yulmwu in https://github.com/nullforu/smctf/pull/27
- Add CTF start and end time features by @yulmwu in https://github.com/nullforu/smctf/pull/29
- Add Redis caching for App Config by @yulmwu in https://github.com/nullforu/smctf/pull/31
```

**Full Changelog**: https://github.com/nullforu/smctf/commits/v1.0.0
