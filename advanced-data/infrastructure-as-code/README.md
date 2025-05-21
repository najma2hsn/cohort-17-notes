# Infrastructure as Code (IaaC)

- The cloud is complex and fiddly
- Remembering the exact steps you took to set something up us hard
- Store your cloud config/setup as code instead of trying to handle it all yourself
- IaaC is maintainable, shareable, and repeatable

## Terraform

Terraform is an "infrastructure as code" tool.

Terraform is a **CONFIG TOOL**, not a programming language.

### Documentation

- [Terraform](https://developer.hashicorp.com/terraform/docs)
- [AWS on Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

### Setup

- Create a `.gitignore` with the appropriate paths
- Create a `main.tf` with a `provider` block
- Run `terraform init` to get Terraform ready to work
- Define resources inside the `main.tf` file
- Run `terraform plan` to see what resources would be created
- Run `terraform apply` to create/update resources (additive)
- Run `terraform destroy` to unmake all resources 

### DB stub

```tf
resource "aws_db_instance" "museum-db" {
    allocated_storage            = 10
    db_name                      = ""
    identifier                   = ""
    engine                       = "postgres"
    engine_version               = "16.1"
    instance_class               = "db.t3.micro"
    publicly_accessible          = true
    performance_insights_enabled = false
    skip_final_snapshot          = true
    db_subnet_group_name         = ""
    vpc_security_group_ids       = []
    username                     = ""
    password                     = ""
}
```