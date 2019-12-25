#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import path
import argparse
import sys

def unix_dirname(pathname):
    '''A unix-behavior dirname function'''
    dirn = pathname
    if not dirn:
        return '.'

    dirn = dirn.rstrip('/')
    if not dirn:
        return '/'
    else:
        dirn = path.dirname(dirn)
        if dirn.find('/') == -1:
            return '.'
    dirn = dirn.rstrip('/')
    if not dirn:
        return '/'
    return dirn

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Strip non-directory suffix from FILENAME',
                                     usage='dirname.py FILENAME')
    parser.add_argument('FILENAME', help='Pathename')
    args = parser.parse_args()
    pathname = args.FILENAME
    
    print(unix_dirname(pathname))
