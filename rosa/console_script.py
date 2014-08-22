#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from os import path
import create_workspace
import merge_rosinstall
import build_rosinstall

def get_parser():
    parser = argparse.ArgumentParser(description='Helpful commands for performing common ROS tasks.')
    parser.add_argument('-w', '--workspace', metavar='FOLDER', type=str,
            help='workspace for operation')
    subparsers = parser.add_subparsers()

    create_workspace.add_parser(subparsers)
    merge_rosinstall.add_parser(subparsers)
    build_rosinstall.add_parser(subparsers)
    return parser

def main():
    args = get_parser().parse_args()
    args.func(args)
