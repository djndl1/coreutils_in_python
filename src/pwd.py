#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import argparse


def unix_pwd(args):
    '''a unix-conformant pwd'''
    pwd_logical = os.getenv('PWD')
    pwd_physical = os.path.abspath(os.getcwd())
    path_max = os.pathconf('.', 'PC_PATH_MAX')

    if not pwd_logical or len(pwd_logical) > path_max:
        pwd_logical = pwd_physical
    if pwd_logical.find('/./') != -1 or pwd_logical.find('/../') != -1 \
       or pwd_logical.endswith('/..') or pwd_logical.endswith('/.') \
       or pwd_logical.startswith('../') or pwd_logical.startswith('./'):
        pwd_logical = pwd_physical
    
    if args.P and args.L:
        for arg in reversed(sys.argv):
            if arg == '-L':
                return pwd_logical
            elif arg == '-P':
                return pwd_physical
    elif args.P:
        return pwd_physical
    else:
        return pwd_logical

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print the full filename of the current working directory',
                                     usage='pwd [-LP]')
    parser.add_argument('-L', help='print the value of $PWD if it names the current working directory (default)',
                        action='store_true')
    parser.add_argument('-P', help='print the physical directory, without any symbolic links',
                        action='store_true')
    args = parser.parse_args()
    print(unix_pwd(args))
