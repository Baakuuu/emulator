import shlex
import sys


vfsName="demo_vfs"
while True:
    a= input(vfsName+ " ")
    b=shlex.split(a)
    cmd = b[0]
    args = b[1:]
    if (cmd == "ls"):
        print(cmd,args)
    elif(cmd == "cd"):
        print(cmd,args)
    elif(cmd == "exit"):
        sys.exit(0)
    else:
        print("Unknown command: ",cmd)
