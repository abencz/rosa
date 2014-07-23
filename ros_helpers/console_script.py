#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
from ros_helpers.create_workspace import create_workspace

def print_usage():
    usage = """Usage:
    %s create_workspace <path>\n""" % path.basename(sys.argv[0])

    sys.stderr.write(usage)
    sys.exit(1)

def main():
    argv = sys.argv
    if len(argv) < 3:
        print_usage()

    command = argv.pop(1)

    if command != 'create_workspace':
        print_usage()

    create_workspace(argv.pop(1))
