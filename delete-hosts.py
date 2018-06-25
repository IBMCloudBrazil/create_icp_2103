#!/usr/bin/python 
import socket
import fcntl
import struct
import os

def play_book ( pb, inv ):
  "run playbook"
  book = "ansible-playbook " + pb +  " -i " +  inv
  os.system(book)
  return

play_book("./playbook/delete.yml","./hostnames.txt")
