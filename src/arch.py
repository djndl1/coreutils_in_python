#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print system architecture')
    args = parser.parse_args()
    print(os.uname().machine)
