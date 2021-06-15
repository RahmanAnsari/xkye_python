#!/usr/bin/env python3

"""
A simple example python file
"""

import os
from xkye import IO as io


def main():

    """ Example python implementation for XKYE Library"""
    xky_file = "example1.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xky_file = dir_path + "/" + xky_file

    xfile = io(xky_file)
    xfile.read()

    print(xfile.get("pgadmin"))
    print(xfile.get("pgadminpwd"))
    print(xfile.get("pghost"))
    print(xfile.get("pgport"))
    print(xfile.get("pgadmindb"))

    print(xfile.get("adminpwd"))
    print(xfile.get("dwzypwd"))

    print(xfile.get("shardid"))
    print(xfile.get("dwzyuser"))
    print(xfile.get("dwzydb"))

    print(xfile.getSpan("shard"))


if __name__ == '__main__':
    main()
