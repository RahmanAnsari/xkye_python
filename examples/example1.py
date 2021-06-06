#!/usr/bin/env python3

"""
A simple example python file
"""

import os
from xkye import IO as io

def main():

    xkyFile = "example1.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    print(xkyFile)

    x = io(xkyFile)
    x.read()

    print(x.get("pgadmin"))
    print(x.get("pgadminpwd"))
    print(x.get("pghost"))
    print(x.get("pgport"))
    print(x.get("pgadmindb"))

    print(x.get("adminpwd"))
    print(x.get("dwzypwd"))

    print(x.get("shardid"))
    print(x.get("dwzyuser"))
    print(x.get("dwzydb"))

if __name__ == '__main__':
    main()

