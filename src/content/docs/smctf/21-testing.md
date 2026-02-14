---
title: 21. 백엔드 유닛/통합 테스팅 및 CI 설정
sidebar:
    order: 125
---

SMCTF의 백엔드는 안정성을 고려하여 TDD 위주로 개발되고 있으며, 유닛 테스트 및 통합 테스트 모두 포함합니다. Codecov 리포트를 확인하려면 아래의 링크를 참조하세요.

- https://app.codecov.io/github/nullforu/smctf

또한 Codecov 커버리지 업로드를 위한 CI가 GitHub Actions로 설정되어 있습니다. `.github/workflows/backend-test-ci.yml` 파일을 참조하세요.

```yaml
name: Backend Test CI

on:
  push:
    branches: [ main ]
    paths:
      - 'cmd/**'
      - 'internal/**'
      - 'go.mod'
      - 'go.sum'
      - 'go.work'
      - '.github/workflows/**'

  pull_request:
    branches: [ main ]
    paths:
      - 'cmd/**'
      - 'internal/**'
      - 'go.mod'
      - 'go.sum'
      - 'go.work'
      - '.github/workflows/**'

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-go@v6
        with:
          go-version: '1.25'
          cache: true

      - name: Run tests with coverage
        run: go test -p=1 -v -coverprofile=coverage.out ./...

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v5
        with:
          files: coverage.out
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}
```
