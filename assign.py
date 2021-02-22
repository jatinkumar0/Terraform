import os

'''p_name = str(input("Enter Project Name : "))
cidr   = str(input("Enter CIDR for VPC : "))
p_cidr = str(input("Enter CIDR for Public Subnet : "))
pr_cidr = str(input("Enter CIDR for Private Subnet : "))
gr_cidr = str(input("Enter Group Subnet CIDR for RDS : "))

terraformtfvars = variables.tf.replace("10.0.0.0/16",cidr)
terraformtfvars = variables.tf.replace("10.0.1.0/24",p_cidr)
terraformtfvars = variables.tf.replace("10.0.0.0/24",pr_cidr)
terraformtfvars = variables.tf.replace("10.0.3.0/24",gr_cidr)
terraformtfvars = variables.tf.replace("kp",project)
file.write(terraformtfvar)
file.close()'''


print("Enter 1 for Project Creation / Enter 0 to delete Resources")
opt = int(input())
if(opt == 1):



    variables="""
    variable "vpc_name" {
    }
    variable "cidr_block" {
    }
    variable "igw_name" {
    }
    variable "nat_instance" {
    }
    variable "public_instance" {
    }
    variable "private_instance" {
    }

    variable "cc" {
    }

"""
    file = open("variables.tf", "w")
    file.write(variables)
    file.close()

    '''terraformtfvars=region = "ap-south-1"
    environment_name = "dev"
    project_name = "abc"
    cidr_block = "10.0.1"
    pub_cidr = "10.0.2"
    terraformtfvars =terraformtfvars.replace("10.0.1",cidr)
    terraformtfvars = terraformtfvars.replace("10.0.2",p_cidr)
    terraformtfvars = terraformtfvars.replace("10.0.0.0/24",pr_cidr)
    terraformtfvars = terraformtfvars.replace("10.0.3.0/24",gr_cidr)
    terraformtfvars = terraformtfvars.replace("abc",p_name)
    file = open("terraform.tfvars", "w")'''
    #os.system('terraform init')
    #os.system('terraform apply')
    #os.system('terraform plan')
    os.system('terraform apply')
