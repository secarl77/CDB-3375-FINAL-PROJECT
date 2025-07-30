terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "5.81.0"
        }
    }
}
provider "aws" {
    region = "ca-central-1"

}

# Create VPC

resource "aws_vpc" "CDB_3375_vpc" {
    cidr_block = "10.0.0.0/16"
    enable_dns_support = true
    enable_dns_hostnames = true

    tags = {
        Name = "CDB-3375-Final-Project-vpc"
    }
}

