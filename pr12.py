import shlex
import sys
import os
import argparse
import pathlib
file_path = os.path.abspath(__file__)
directory_path= "."
vfsName="demo_vfs"
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vfs-path", required=True)
    parser.add_argument("--prompt", default="> ")
    parser.add_argument("--startup-script")
    args = parser.parse_args()

    if not os.path.isdir(args.vfs_path):
        print("Error: VFS path is invalid", file=sys.stderr)
        sys.exit(1)


    print("=== Emulator Configuration ===")
    print(f"VFS Path:        {os.path.abspath(args.vfs_path)}")
    print(f"Prompt:          {repr(args.prompt)}")
    print(f"Startup Script:  {args.startup_script or 'None'}")
    print("==============================\n")

while True:
    a= input(vfsName + " " + file_path + "\n")
    b=shlex.split(a)
    cmd = b[0]
    args = b[1:]
    if (cmd == "ls"):
        print(cmd,args)
    elif(cmd == "cd"):
        print(cmd,args)
    elif(cmd == "exit"):
        sys.exit(0)
    elif(cmd =="dir"):
        direc= os.listdir(directory_path)
        print(cmd,direc)
    elif(cmd == "cls"):
        os.system('cls')
    else:
        print("Unknown command: ",cmd)