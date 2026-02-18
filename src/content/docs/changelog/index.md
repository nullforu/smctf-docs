---
title: SMCTF Changelog
sidebar:
    order: 1
---

### v1.1.0 (2026-02-18)

`v1.0.0` 릴리즈 이후 몇가지 개선과 기능 추가, 버그 수정을 포함한 릴리즈입니다. `v1.0.0`과 호환되지 않는 API 변경이 포함되어 있습니다.

---

- 가입 키(Registration Key)가 6자리 숫자가 아닌 16자리의 랜덤한 문자열로 변경되었으며, 일회성이 아닌 다회용으로 사용할 수 있도록 최대 사용 횟수 기능이 추가되었습니다. 
- 자세한 내용은 업데이트된 [가입 인증 키 관리](/smctf/admin/6-key-manage) 문서를 참조하세요. PR [#32](https://github.com/nullforu/smctf/pull/32)

---

- 유저에 대한 팀 이동 기능이 추가되었습니다. 관리자 페이지에서 특정 유저의 팀을 변경할 수 있습니다.
- 유저에 대한 제한(차단) 및 제한 해제 기능이 추가되었습니다. 차단된 유저는 문제 풀이가 불가하고 스코어보드에 반영되지 않습니다. 
- 자세한 내용은 업데이트된 [유저](/smctf/7-users) 및 [유저 관리](/smctf/admin/3-user-manage) 문서를 참조하세요. PR [#33](https://github.com/nullforu/smctf/pull/33)

---

- 관리자는 모든 스택을 조회하고 직접 삭제할 수 있습니다.
- 자세한 내용은 업데이트된 [스택 관리](/smctf/admin/5-stack-manage) 문서를 참조하세요. PR [#36](https://github.com/nullforu/smctf/pull/36)

---

- 관리자는 대회 보고서(리포트)를 생성할 수 있습니다. 이는 JSON 또는 YAML 형태로 제공되며, 추후 PDF 형태로도 제공될 예정입니다.
- 자세한 내용은 업데이트된 [대회 보고서(리포트)](/smctf/admin/8-report) 문서를 참조하세요. PR [#37](https://github.com/nullforu/smctf/pull/37)

---

이에 따른 관련된 프론트엔드 UI 수정 또는 개선이 이루어졌습니다.

- 문제 목록(`/challenges`) 페이지에서 카테고리별 그룹화 기능이 추가되었습니다.
- 일부 편집 가능한 항목에서 [Monaco Editor](https://microsoft.github.io/monaco-editor/)를 도입하였습니다.
- 관리자 페이지의 UI/UX가 개선되었으며 유저 관리, 스택 관리 및 보고서 생성과 관련된 탭이 추가되었습니다.

프론트엔드([nullforu/smctfe](https://github.com/nullforu/smctfe))는 백엔드와 별도의 저장소에서 관리되며 별도의 버전 릴리즈가 이루어집니다.
때문에 위 내용은 백엔드의 공식 릴리즈엔 포함되지 않지만 관련된 프론트엔드 업데이트임에 따라 함께 언급합니다.

---

그 밖에 아래와 같이 리펙토링이 이루어졌습니다. 자세한 내용은 각 PR 내용을 참조하세요.

* Normalize app config/challenge update API semantics and expand test coverage. [#35](https://github.com/nullforu/smctf/pull/35)
* Refactoring before v1.1.0 release. PR [#38](https://github.com/nullforu/smctf/pull/38)

### v1.0.0 (2026-02-15) (Pre Release)

SMCTF의 첫번째 공식 릴리즈로, Pre Release로 배포되었습니다. 
`v1.1.0` 이후 추가된 기능을 제외한 모든 기능이 포함되어 있으며, 몇몇 API가 `v1.1.0` 이상과 호환되지 않을 수 있습니다. 

```md
* chore(deps): bump esbuild, @sveltejs/vite-plugin-svelte and vite in /frontend by @dependabot[bot] in https://github.com/nullforu/smctf/pull/2
* chore(deps): bump github.com/quic-go/quic-go from 0.54.0 to 0.57.0 by @dependabot[bot] in https://github.com/nullforu/smctf/pull/1
* Add unit test and/or integration test coverage by @yulmwu in https://github.com/nullforu/smctf/pull/5
* fix: codecov comment behavior to default by @yulmwu in https://github.com/nullforu/smctf/pull/7
* Add db, repo and config package unit test coverage by @yulmwu in https://github.com/nullforu/smctf/pull/8
* Add file logging and Discord/Slack webhook logging by @yulmwu in https://github.com/nullforu/smctf/pull/10
* Add group/organization features by @yulmwu in https://github.com/nullforu/smctf/pull/12
* Added README preview images and chore script and frontend by @yulmwu in https://github.com/nullforu/smctf/pull/13
* Add team features by @yulmwu in https://github.com/nullforu/smctf/pull/15
* Add dynamic scoring feature  by @yulmwu in https://github.com/nullforu/smctf/pull/16
* Chore/update dummy sql generator scripts  by @yulmwu in https://github.com/nullforu/smctf/pull/17
* Add UI customization features by @yulmwu in https://github.com/nullforu/smctf/pull/19
* Add challenge file upload/download via AWS presigned url by @yulmwu in https://github.com/nullforu/smctf/pull/21
* Remove the "not affiliated with any team" feature for users. by @yulmwu in https://github.com/nullforu/smctf/pull/23
* Leaderboard improvements and First Blood feature addition by @yulmwu in https://github.com/nullforu/smctf/pull/24
* Implement Stack Instance in the SMCTF service using the Container Provisioner microservice by @yulmwu in https://github.com/nullforu/smctf/pull/25
* Improve and optimize frontend UI/UX and add internationalization by @yulmwu in https://github.com/nullforu/smctf/pull/27
* Add CTF start and end time features by @yulmwu in https://github.com/nullforu/smctf/pull/29
* Add Redis caching for App Config by @yulmwu in https://github.com/nullforu/smctf/pull/31
```

**Full Changelog**: https://github.com/nullforu/smctf/commits/v1.0.0
