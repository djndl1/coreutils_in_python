#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import path
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Strip directory path and .SUFFIX from FILE',
                                     usage='basename.py FILE [SUFFIX]')
    parser.add_argument('FILE', help='Pathname')
    parser.add_argument('SUFFIX', help='File suffix', nargs='?', default='')
    args = parser.parse_args()
    pathname = args.FILE
    suffix = args.SUFFIX

    
    if (not pathname) or pathname == '/':
        print()
        sys.exit(0)
    basename = pathname.rstrip('/')
    
    if not basename:
        basename = '/'
    else:
        basename = path.basename(basename)

    if suffix and basename != suffix and basename.endswith(suffix):
        basename = basename[:-len(suffix)]

    print(basename)
    
