---
title: 17. Dynamic Scoring
sidebar:
    order: 105
---

SMCTF는 CTF 대회에서 참가자들의 점수를 기반으로 문제의 난이도를 동적으로 계산하여 점수를 조정하는 Dynamic Scoring(Value) 기능을 기본적으로 적용합니다.

이는 CTFd의 Dynamic Value와 동일한 공식으로 구현되었으며, 그 공식은 아래와 같습니다.

- Initial - 문제의 기본 점수
- Minimum - 문제의 최소 점수
- Decay - 문제가 최소 점수에 도달하기까지의 풀이 수 (= 팀 수)

위 값을 기반으로 점수는 아래와 같이 계산됩니다.

```
value = (((minimum - initial) / (decay ** 2)) * (solve_count ** 2)) + initial
value = math.ceil(value)
```

초기 값이 500, 최고 값이 100에 50 팀이 존재한다고 가정한다면 아래와 같이 풀이 수에 따른 점수의 변화를 시뮬레이션할 수 있습니다.

```py
0 solves 500 points
1 solves 500 points
2 solves 500 points
3 solves 499 points
4 solves 498 points
5 solves 496 points
...
48 solves 132 points
49 solves 116 points
50 solves 100 points
```

이는 CTFd의 Dynamic Value와 동일한 공식으로 구현되었으며, 아래의 문서를 참조하세요.

- https://docs.ctfd.io/docs/custom-challenges/dynamic-value
