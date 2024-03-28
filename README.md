# Cloudformation | ansible | packer

Project Summary:

This project aims to automate the deployment of a web application using AWS CloudFormation for infrastructure provisioning and Ansible for configuration management. The project consists of three main components:

1. CloudFormation Script:
The CloudFormation script creates the following AWS components:
- Virtual Private Cloud (VPC) with two public and private subnets
- Route tables for each subnet
- Security Group to allow traffic on port 80 and 443
- Elastic Load Balancer (ELB) and Application Load Balancer (ALB)
- Private Route53 hosted zone and CNAME entries for both ALB and ELB
- IAM Policy for assignment-3

2. Ansible Playbook:
The Ansible playbook performs the following tasks:
- Selects a Linux AMI
- Installs a web server (Apache/Nginx)
- Downloads code from a Git repository
- Configures the web server with security best practices (e.g., disabling directory listing, limiting server tokens)
- Creates a self-signed certificate for HTTPS
- Secures a demo site using the self-signed certificate

3. Execution of Ansible Playbook:
The Ansible playbook is executed in a Packer job to create a custom Amazon Machine Image (AMI). The AMI is then used to automatically create an Auto Scaling Group (ASG) and attach it to the ELB. The project showcases the capabilities of the ALB by implementing two different domain routing policies. Instances launched behind the ELB/ALB have a role attached, granting access to a specific S3 bucket to pull images from.

Overall, this project demonstrates the automation of infrastructure deployment and configuration management using CloudFormation and Ansible, showcasing best practices for security and scalability in a cloud environment.
