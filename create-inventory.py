#!/usr/bin/python 
import os
import subprocess
import time

#def sl_ready( vs ):
#   "slcli"
#   output = subprocess.check_output("slcli vs ready " + vs, shell=True)
#   return (output)

def sl_ip( host ):
   "slcli"
   output = os.system("slcli vs detail " + host + " | grep public  | awk '{ print $2 }' >> ./.ips.txt")
   return (output)

with open('hostnames.txt') as f:
   for line in f:
       sl_ip(line.rstrip())
       #print line
       if 'str' in line:
          break