#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import os
import argparse
from os import path
from .merge_rosinstall import merge_into_workspace

def create_workspace(args):
    try:
        from catkin.init_workspace import init_workspace
    except ImportError:
        sys.stderr.write("Cannot import catkin libraries. Did you source setup.{sh,bash,zsh}?\n")
        sys.exit(os.EX_UNAVAILABLE)

    workspace = path.abspath(args.path[0])
    if path.exists(workspace):
        if path.isdir(workspace):
            sys.stderr.write("Path %s already exists\n" % workspace)
        else:
            sys.stderr.write("File/symlink exists at %s\n" % workspace)
        sys.exit(os.EX_CANTCREAT)

    workspace_src = path.join(workspace, "src")
    os.makedirs(workspace_src)

    try:
        init_workspace(workspace_src)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(2)

    if args.i:
        merge_into_workspace(workspace, args.i)


def add_parser(parent_subparsers):
    parser = parent_subparsers.add_parser('create_workspace', 
            description='Create a new ROS workspace.')
    parser.add_argument('-i', metavar='URI', action='append', type=str,
            help='initialize with one or more rosinstalls')
    parser.add_argument('path', metavar='FOLDER', type=str, nargs=1,
            help='path of newly created workspace')
    parser.set_defaults(func=create_workspace)
