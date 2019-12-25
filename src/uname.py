#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import argparse

def unix_uname(args):
    uinfo = os.uname();
    if args.a:
        uname_str = uinfo.sysname + ' ' + uinfo.nodename + ' ' + \
            uinfo.release + ' ' + uinfo.version + ' ' + uinfo.machine
        return uname_str
              
    info_str = []
    if args.s:
        info_str.append(uinfo.sysname)
    if args.n:
        info_str.append(uinfo.nodename)
    if args.r:
        info_str.append(uinfo.release)
    if args.v:
        info_str.append(uinfo.version)
    if args.m:
        info_str.append(uinfo.machine)
    if not info_str:
        info_str.append(uinfo.sysname)
    fmt_str = info_str[0]
    for s in info_str[1:]:
        fmt_str = fmt_str + ' ' + s;
    return fmt_str

if __name__ == '__main__':
    fmt_parser = argparse.ArgumentParser(description='Print system information');
    fmt_parser.add_argument('-a', help='Print all information',
                            action='store_true')
    fmt_parser.add_argument('-m', help='Hardware identifier',
                            action='store_true')
    fmt_parser.add_argument('-n', help='Name of machine on network',
                            action='store_true')
    fmt_parser.add_argument('-r', help='Operating system release',
                            action='store_true')
    fmt_parser.add_argument('-s', help='Operating system name (default)',
                            action='store_true')
    fmt_parser.add_argument('-v', help='Operating system version',
                            action='store_true')
    args = fmt_parser.parse_args()
    print(unix_uname(args))
