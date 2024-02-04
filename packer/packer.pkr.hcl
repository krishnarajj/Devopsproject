packer {
  required_plugins {
    amazon = {
      version = ">= 1.3.0"
      source  = "github.com/hashicorp/amazon"
    }
  }
}



source "amazon-ebs" "ubuntu" {
  access_key    = ""
  secret_key    = ""
  ami_name      = "webserverimg-3"
  instance_type = "t2.micro"
  region        = "us-east-1"
  source_ami    = "ami-0c7217cdde317cfec"
  ssh_username  = "ubuntu"
}

build {
  name = "my-web-build"
  sources = [
    "source.amazon-ebs.ubuntu"
  ]
  # Install Ansible
  provisioner "shell" {
    script = "scripts/ansible.sh"
  }

  provisioner "ansible-local" {
    playbook_file   = "ansible/playforpacker.yaml"
    extra_arguments = ["-vvvv"]
  }


  provisioner "shell" {
    script = "scripts/cleanup.sh"
  }

}