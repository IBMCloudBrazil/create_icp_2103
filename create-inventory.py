#!/usr/bin/python 
import socket
import fcntl
import struct
import os


def hosts():
   "slcli"
   slcli = "slcli vs list | awk '{ print $3 }' > ./ip-hosts.txt" 
   os.system(slcli)
   return

hosts()

with open( "./ip-hosts.txt", 'r') as fin:
    print fin.read()
