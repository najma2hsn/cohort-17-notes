# Where/how are you creating the resources?

provider "aws" {
    region = var.AWS_REGION
    access_key = var.AWS_ACCESS_KEY
    secret_key = var.AWS_SECRET_KEY
}

# Establish which resources you already know about

data "aws_vpc" "current-vpc" {
    id = "vpc-00b3f6b2893c390f2"
}

data "aws_db_subnet_group" "subnet-group" {
    name = "c17-public-subnet-group"
}

# Define cloud resources to create/manage

resource "aws_s3_bucket" "example-bucket" {
    bucket = "c17-dan-example-bucket-better"
    force_destroy = true
}

resource "aws_security_group" "db-security-group" {
    name = "c17-dan-museum-db-sg"
    vpc_id = data.aws_vpc.current-vpc.id
}

resource "aws_vpc_security_group_ingress_rule" "db-sg-inbound-rule" {
    security_group_id = aws_security_group.db-security-group.id
    cidr_ipv4   = "0.0.0.0/0"
    from_port   = 5432
    ip_protocol = "tcp"
    to_port     = 5432
}


resource "aws_db_instance" "museum-db" {
    allocated_storage            = 10
    db_name                      = "postgres"
    identifier                   = "c17-dan-example-rds"
    engine                       = "postgres"
    engine_version               = "17"
    instance_class               = "db.t3.micro"
    publicly_accessible          = true
    performance_insights_enabled = false
    skip_final_snapshot          = true
    db_subnet_group_name         = data.aws_db_subnet_group.subnet-group.name
    vpc_security_group_ids       = [aws_security_group.db-security-group.id]
    username                     = var.DB_USERNAME
    password                     = var.DB_PASSWORD
}