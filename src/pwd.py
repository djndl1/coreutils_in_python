#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

def pwd(args):
    pwd_logical = os.getenv('PWD')
    pwd_physical = os.getcwd()

    args_r = reversed(args)
    for arg in args_r:
        if arg == '-P':
            return pwd_physical
        
    return pwd_logical

if __name__ == '__main__':
    pwd = pwd(sys.argv)
    print(pwd)