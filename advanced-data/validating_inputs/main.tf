provider "aws" {
    region = var.AWS_REGION
    access_key = var.AWS_ACCESS_KEY
    secret_key = var.AWS_SECRET_KEY
}

data "aws_vpc" "current-vpc" {
    id = "vpc-00b3f6b2893c390f2"
}

data "aws_subnet" "ec2-subnet" {
  id = var.AWS_SUBNET
}

resource "aws_security_group" "c17-example-sg" {
  name   = "c17-example-sg"
  vpc_id = data.aws_vpc.current-vpc.id

}

resource "aws_vpc_security_group_ingress_rule" "ec2-inbound-rule" {
    security_group_id = aws_security_group.c17-example-sg.id
    cidr_ipv4   = "0.0.0.0/0"
    from_port   = 5432
    ip_protocol = "tcp"
    to_port     = 5432
}

resource "aws_vpc_security_group_egress_rule" "example" {
  security_group_id = aws_security_group.c17-example-sg.id
    cidr_ipv4   = "0.0.0.0/0"
    from_port   = 5432
    ip_protocol = "tcp"
    to_port     = 5432
}

resource "aws_instance" "example" {
  ami           = "ami-0dfe0f1abee59c78d"
  instance_type = "t2.nano"
  subnet_id     = data.aws_subnet.ec2-subnet.id
  associate_public_ip_address = true
  security_groups = [aws_security_group.c17-example-sg.name]

  cpu_options {
    core_count       = 1
    threads_per_core = 1
  }

  tags = {
    Name = "ec2-example"
  }
}