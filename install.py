#!/usr/bin/python 
import socket
import fcntl
import struct
import os

def git ( url ):
   " using git"
   gt = "git clone " + url
   os.system(gt)
   return

def play_book ( pb, inv ):
  "run playbook"
  book = "ansible-playbook " + pb +  " -i " +  inv
  os.system(book)
  return

def docker_run ( dexec ):
  "run docker"
  ds = "/usr/bin/docker run " + dexec
  os.system(ds)
  return

def apt ( pkg ):
   "install via apt"
   install = "apt install -y  " + pkg
   os.system(install)
   return

ip=socket.gethostbyname(socket.gethostname())
hostname=socket.gethostname()

apt("ansible")
git("https://github.com/IBMCloudBrazil/create_icp_2103.git")

file = open("/opt/ibm-cloud-private-ce-2.1.0.3/cluster/hosts", "w")
file.write("")
file.close()

file = open("/root/criar_ambiente_icp/inventory", "w")
file.write("[minicloud]\n")
file.write( hostname + " ansible_ssh_host=" + ip + "\n")
file.close()


play_book("/root/criar_ambiente_icp/hosts.yml","/root/criar_ambiente_icp/inventory")
docker_run("-e LICENSE=accept --net=host  -t -v /opt/ibm-cloud-private-ce-2.1.0.3/cluster:/installer/cluster ibmcom/icp-inception:2.1.0.3 install")