#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import argparse

from os import path

def merge_into_workspace(workspace, uris):
    try:
        from wstool.multiproject_cli import prompt_merge
        from wstool.multiproject_cmd import cmd_persist_config
    except ImportError:
        print("Cannot import wstool libraries. Did you source setup.{sh,bash,zsh}?")
        sys.exit(os.EX_UNAVAILABLE)

    rosinstall_name = '.rosinstall'
    rosinstall_path = path.join(workspace, 'src')
    if not path.isdir(rosinstall_path):
        print("%s is not a valid workspace" % workspace)
        sys.exit(1)

    if not path.exists(path.join(rosinstall_path, rosinstall_name)):
        with file(path.join(rosinstall_path, rosinstall_name), 'w') as f:
            f.write('\n')

    (newconfig, _) = prompt_merge(rosinstall_path,
            additional_uris=uris,
            additional_specs=[],
            confirmed=True,
            config_filename=rosinstall_name)

    cmd_persist_config(newconfig, rosinstall_name)


def merge_rosinstall(args):
    merge_into_workspace(args.workspace[0], args.rosinstalls)


def add_parser(parent_subparsers):
    parser = parent_subparsers.add_parser('merge_rosinstall', 
            description='Merge rosinstall into a ROS workspace')
    parser.add_argument('workspace', metavar='FOLDER', type=str, nargs=1,
            help='Path to a ROS workspace')
    parser.add_argument('rosinstalls', metavar='URI', type=str, nargs='+',
            help='URI or rosinstall to be merged')
    parser.set_defaults(func=merge_rosinstall)