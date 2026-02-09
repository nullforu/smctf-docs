---
title: REST API 문서
---

> 작성 중인 문서입니다. 추후 더욱 더 세부적인 내용이 추가될 예정입니다.

- Base URL: `http://<HOST>:8081`

## Health

- `GET /healthz`
- Response

```json
{
  "status": "ok"
}
```

## Stack APIs

### Create Stack

- `POST /stacks`
- Body

```json
{
  "target_port": 5000,
  "pod_spec": "apiVersion: v1\nkind: Pod\nmetadata:\n  name: problem-1001\nspec:\n  containers:\n    - name: app\n      image: ghcr.io/example/problem:latest\n      ports:\n        - containerPort: 5000\n          protocol: TCP\n      resources:\n        requests:\n          cpu: \"500m\"\n          memory: \"256Mi\"\n        limits:\n          cpu: \"500m\"\n          memory: \"256Mi\"\n"
}
```

- Success: `201 Created`
- Response includes `node_public_ip` (null when the node has no public IP).

### List All Stacks

- `GET /stacks`
- Success: `200 OK`
- Each stack includes `node_public_ip` (null when the node has no public IP).

### Get Stack

- `GET /stacks/{stack_id}`
- Success: `200 OK`
- Response includes `node_public_ip` (null when the node has no public IP).

### Get Stack Status

- `GET /stacks/{stack_id}/status`
- Success: `200 OK`
- Response fields:
  - `stack_id`
  - `status`
  - `ttl`
  - `node_port`
  - `target_port`
  - `node_public_ip`

### Delete Stack

- `DELETE /stacks/{stack_id}`
- Success: `200 OK`

### Stats

- `GET /stats`
- Success: `200 OK`

## Error codes

- `400`: invalid request body / pod spec validation error
- `400`: Kubernetes `LimitRange` violation
- `404`: stack not found
- `503`: cluster saturation, no available nodeport
- `503`: Kubernetes `ResourceQuota` violation
- `500`: internal server error
