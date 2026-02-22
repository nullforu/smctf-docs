---
title: 4. Terraform 구성
sidebar:
    order: 4
---

인프라 운영자의 입장에서 다양한 옵션을 쉽게 커스터마이징 할 수 있도록 다양한 Terraform Variables를 제공합니다. 
이 문서에선 존재하는 모든 옵션들에 대해 세부적으로 설명하기 보다는 기능별로 주요 옵션들에 대해 설명합니다.

Terraform IaC(HCL)에 대해선 직접 [nullforu/smctf-infra 레포지토리](https://github.com/nullforu/smctf-infra)를 참조하세요.

`특별한 경우가 아니라면 기본값을 권장한다`라는 표현은 변경시 예상치 못한 트러블이 발생할 수 있는 옵션이거나, 다른 옵션도 함께 변경해야 하는 옵션, 또는 보안상 권장되지 않는 옵션을 의미합니다.

### Terraform 초기화

기본적으로 Terraform 백엔드는 S3 버킷과 DynamoDB 테이블을 사용하여 원격으로 상태 관리를 구성하도록 설계되어 있습니다.
때문에 Terraform을 사용하기 전에 필요한 S3 버킷과 DynamoDB 테이블이 존재하는지 확인해야 합니다. 존재하지 않다면 아래의 스크립트를 통해 생성하세요.

```bash
RANDOM_PREFIX=$(openssl rand -hex 2)
AWS_REGION=ap-northeast-2
BUCKET_NAME=terraform-$RANDOM_PREFIX
DDB_TABLE_NAME=terraform-$RANDOM_PREFIX

aws s3api create-bucket \
  --bucket $BUCKET_NAME \
  --region $AWS_REGION \
  --create-bucket-configuration LocationConstraint=$AWS_REGION

aws dynamodb create-table \
  --table-name $DDB_TABLE_NAME \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region $AWS_REGION

echo "Bucket Name: $BUCKET_NAME"
echo "DynamoDB Table Name: $DDB_TABLE_NAME"
```

생성 후 `main.tf` 파일에서 `backend` 블록의 `bucket`과 `dynamodb_table` 값을 생성한 리소스 이름으로 수정하세요.

```hcl
backend "s3" {
  bucket         = "<BUCKET_NAME>"
  key            = "smctf/terraform.tfstate"
  region         = "ap-northeast-2"
  dynamodb_table = "<DDB_TABLE_NAME>"
  encrypt        = true
}
```

이제 아래의 명령어를 통해 Terraform을 초기화할 수 있습니다.

```bash
terraform init
```

아래부터 Terraform Variables에 대한 설명이 이어집니다. 기본적으로 서울 리전(`ap-northeast-2`)과 2개의 AZ(`ap-northeast-2a`, `ap-northeast-2c`)에 배포하도록 구성되어 있으며, 필요에 따라 수정할 수 있습니다.

다만 기본값은 서울 리전을 기준으로 설정되어 있기 때문에 이에 대한 트러블이 발생할 수 있습니다. 필요시 적절하게 수정하여 사용하세요.

### Terraform 적용

기본적으로 `terraform.tfvars`로 구성하면 자동으로 인식하지만, 환경 분리 시 별도의 tfvars 파일을 만들어 적용할 수 있습니다. (예: `terraform apply -var-file="dev.tfvars"`)

```bash
terraform apply -var-file="terraform.tfvars"
```

또는 아래와 같이 특정 모듈이나 리소스만 타겟으로 적용할 수도 있습니다. (예: ECR 리포지토리만 생성)

```bash
terraform init -backend=false
terraform apply -var-file="terraform.tfvars" -target=module.storage.aws_ecr_repository.repos

ECR_REPO_URLS_JSON=$(terraform output -json ecr_repository_urls)
echo "$ECR_REPO_URLS_JSON"
```

### 프로젝트 및 환경 구성

```hcl
project     = "smctf"
environment = "dev"
region      = "ap-northeast-2"
azs         = ["ap-northeast-2a", "ap-northeast-2c"]

common_tags = {}
```

- 리소스의 이름은에서 접두사는 `${var.project}-${var.environment}`로 구성됩니다. 중복되지 않도록 주의하세요.
- `common_tags`는 모든 리소스에 적용되는 공통 태그입니다. 필요시 적절하게 수정하여 사용하세요.

### 네트워크 구성

```hcl
vpc_cidr               = "10.0.0.0/16"
public_subnet_cidrs    = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnet_cidrs   = ["10.0.11.0/24", "10.0.21.0/24"]
protected_subnet_cidrs = ["10.0.111.0/24", "10.0.121.0/24"]

nat_gateway_mode = "single"
```

- VPC CIDR와 서브넷 CIDR은 기본값으로 설정되어 있지만 필요에 따라 수정할 수 있습니다. 다만 CIDR이 겹치지 않도록 주의하세요.
- NAT Gateway는 `single` 또는 `per_az` 모드로 배포할 수 있습니다. `single` 모드는 단일 NAT Gateway를 배포하여 비용 효율성을 높이는 옵션이고, `per_az` 모드는 각 AZ마다 NAT Gateway를 배포하여 가용성을 높이는 옵션입니다. 특별한 경우가 아니라면 단일 NAT Gateway를 배포하는 `single` 모드를 권장합니다.

### EKS 클러스터 구성

```hcl
eks_cluster_name            = "smctf"
eks_version                 = "1.35"
eks_endpoint_public_access  = true
eks_endpoint_private_access = true

stack_node_instance_types = ["t3a.medium"]
stack_node_desired_size   = 2
stack_node_min_size       = 1
stack_node_max_size       = 4

backend_node_instance_types = ["t3a.medium"]
backend_node_desired_size   = 2
backend_node_min_size       = 1
backend_node_max_size       = 4

stack_nodeport_cidrs = ["0.0.0.0/0"]
stack_nodeport_range = {
  from = 31001
  to   = 32767
}

backend_nodeport_range = {
  from = 30000
  to   = 31000
}

alb_ingress_cidrs = ["0.0.0.0/0"]
```

- EKS 클러스터 버전은 기본적으로 1.35로 설정되어 있지만 필요에 따라 수정할 수 있습니다. 낮은 버전의 Kubernetes를 사용하는 경우 Extended Support로 인해 추가 비용이 발생할 수 있으니 특별한 경우가 아니라면 최신 버전을 사용하는 것을 권장합니다.
- EKS 클러스터의 API 서버 엔드포인트는 외부에서 kubectl로 접근할 수 있도록 `public_access`가 활성화되어 있습니다. 보안상 권장되진 않지만 VPN이나 관련된 Bastion Host를 구성하지 않았기 때문에 kubectl로 접근하기 위해선 Public Access가 필요합니다.
- 스택 노드와 백엔드 노드는 각각 별도의 Node Group으로 구성되어 있으며, 필요에 따라 인스턴스 유형과 Auto Scaling 그룹의 크기를 조정할 수 있습니다. 이에 대해선 [Container Provisioner](/container-provisioner) 문서를 참조하세요.

그 외의 설정은 기본값을 권장하며 특별한 경우가 아니라면 수정할 필요는 없습니다. 다만 필요에 따라 ALB Ingress의 CIDR을 제한하는 등의 설정을 추가로 구성할 수 있습니다. (예: Cloudflare의 IP 범위)

### RDS 및 ElastiCache 구성

```hcl
rds_instance_class        = "db.t3.micro"
rds_allocated_storage_gb  = 20
rds_multi_az              = false
rds_engine_version        = null
rds_db_name               = "smctf"
rds_master_username       = "smctf_admin"
rds_master_password       = "REPLACE_ME"
rds_backup_retention_days = 7
rds_deletion_protection   = true

redis_node_type       = "cache.t3.micro"
redis_engine_version  = null
redis_multi_az        = false
redis_num_cache_nodes = 1
```

- RDS와 ElastiCache의 인스턴스 유형은 [Container Provisioner](/container-provisioner) 문서를 참조하세요. EKS 노드 및 DB 인스턴스 유형을 선택할 수 있는 가이드가 포함되어 있습니다.
- RDS의 경우 실수로 삭제를 방지하기 위해 `deletion_protection`이 활성화되어 있습니다. RDS 인스턴스를 삭제하려면 먼저 이 설정을 비활성화해야 하며, 삭제 후 자동으로 스냅샷이 생성됩니다.
- 기본적으로 단일 AZ에 배포되도록 구성되어 있지만, 필요에 따라 다중 AZ로 배포하여 가용성을 높일 수 있습니다. 다만 비용이 증가할 수 있으니 특별한 경우가 아니라면 단일 AZ로 배포하는 것을 권장합니다.
- RDS 마스터 비밀번호는 반드시 안전한 값으로 변경하여 사용하세요. 필요시 AWS Secrets Manager와 연동하여 관리하는 것도 고려할 수 있습니다. (Terraform 구성은 직접 수정해야 합니다.)

### S3, ECR, DynamoDB 구성

```hcl
s3_challenge_bucket_name   = "smctf-challenges-bucket"
create_s3_challenge_bucket = false
# s3_cors_rules = [
#   {
#     allowed_headers = ["*"]
#     allowed_methods = ["GET", "PUT", "POST", "DELETE", "HEAD"]
#     allowed_origins = ["https://ctf.swua.kr"]
#     expose_headers  = ["ETag"]
#     max_age_seconds = 3000
#   }
# ]

ecr_repository_names    = ["backend", "container-provisioner", "smctf-challenges"]
create_ecr_repositories = false

dynamodb_table_name           = "smctf-container-provisioner-stacks"
dynamodb_billing_mode         = "PAY_PER_REQUEST"
dynamodb_read_capacity        = 5
dynamodb_write_capacity       = 5
enable_point_in_time_recovery = true
```

- S3 버킷과 ECR 리포지토리는 필요에 따라 생성할 수 있도록 구성되어 있습니다. 미리 만들어둔 리소스가 있다면 해당 이름으로 설정하여 사용할 수 있습니다. 생성하는 옵션을 선택할 시 S3에 대한 CORS 규칙도 함께 구성할 수 있습니다.
- DynamoDB 테이블은 Container Provisioner가 스택 상태를 저장하는데 사용됩니다. 기본값을 권장합니다.

### IRSA 구성

```hcl
irsa_namespace         = "backend"
irsa_alb_namespace     = "kube-system"
irsa_logging_namespace = "logging"
irsa_service_accounts = {
  alb_controller        = "aws-load-balancer-controller"
  container_provisioner = "container-provisioner"
  backend_service       = "smctf-backend"
  fluentbit             = "fluent-bit-cloudwatch"
}

extra_node_role_policy_arns = []
```

- EKS 클러스터 내 리소스가 AWS 리소스에 접근할 수 있도록 IRSA(IAM Roles for Service Accounts)가 기본적으로 구성되어 있습니다. 이는 Kubernetes에서 사용됩니다.
- 모두 기본값을 권장하며, 필요시 추가적인 Node Role 정책 ARN을 `extra_node_role_policy_arns`에 추가하여 노드에서 추가적인 AWS 리소스에 접근할 수 있도록 구성할 수 있습니다.

### EKS 플러그인(애드온) 구성

```hcl
enable_network_policy            = true
vpc_cni_addon_version            = null
vpc_cni_service_account_role_arn = null
coredns_addon_version            = null
```

- EKS 클러스터의 VPC CNI는 기본적으로 NetworkPolicy를 적용하지 못합니다. 이에 따라 Calico NetworkPolicy Agent를 사용하여 NetworkPolicy를 적용할 수 있도록 구성할 수 있지만 AWS VPC CNI에서도 NetworkPolicy Agent를 적용할 수 있도록 구성할 수 있습니다. 특별한 경우가 아니라면 VPC CNI에서 NetworkPolicy를 적용하는 것을 권장합니다.
- 특별한 경우가 아니라면 EKS 플러그인(애드온)의 버전은 기본값을 권장합니다. EKS 클러스터 버전에 맞는 호환되는 버전을 사용하는 것이 중요합니다. 필요시 AWS 문서를 참조하여 호환되는 버전을 확인하세요.

### Bastion Host 구성

```hcl
create_bastion           = false
bastion_instance_type    = "t3.micro"
bastion_ami_id           = null
bastion_subnet_index     = 0
bastion_root_volume_size = 20
bastion_key_name         = null
```

- Bastion Host는 EKS 클러스터의 노드에 접속하거나 DB에 접속하기 위해 옵션에 따라 활성화할 수 있습니다. System Manager의 Session Manager를 통해 접근할 수 있으며, 이와 관련된 IAM 역할 및 VPC 엔드포인트는 기본적으로 구성되어 있습니다. 

### VPC 엔드포인트 구성

```hcl
enable_ssm_vpc_endpoints     = false
enable_s3_vpc_endpoint       = true
enable_dynamodb_vpc_endpoint = true
```

- `enable_ssm_vpc_endpoints`는 Bastion Host가 활성화된 경우에만 활성화하세요. Session Manager를 사용하기 위해 필요한 VPC 엔드포인트입니다.
- S3 및 DynamoDB에 대한 VPC 엔드포인트는 기본적으로 활성화되어 있습니다. 이는 비교적 트래픽이 많은 리소스에 대한 Gateway 엔드포인트입니다.
- 그 외의 리소스에 대한 인터페이스 엔드포인트도 고려하였으나, 비용 효율성 측면에서 NAT Gateway를 같이 사용하는 옵션이 더 낫다고 판단하여 배포 옵션에서 제외하였습니다. 필요 시 직접 Terraform 구성을 수정하여 인터페이스 엔드포인트를 추가할 수 있습니다.

---

EKS 클러스터 생성 후 아래의 명령어를 통해 kubeconfig를 업데이트하여 kubectl로 접근할 수 있습니다.

```bash
aws eks --region ap-northeast-2 update-kubeconfig --name <cluster_name>
```
