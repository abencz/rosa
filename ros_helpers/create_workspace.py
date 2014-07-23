#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os import path

def create_workspace(workspace):
    try:
        from catkin.init_workspace import init_workspace
    except ImportError:
        print "Cannot import catkin libraries. Did you source setup.{sh,bash,zsh}?"
        sys.exit(os.EX_UNAVAILABLE)

    workspace = path.abspath(workspace)
    if path.exists(workspace):
        if path.isdir(workspace):
            print "Path %s already exists" % workspace
        else:
            print "File/symlink exists at %s" % workspace
        sys.exit(os.EX_CANTCREAT)

    workspace_src = path.join(workspace, "src")
    os.makedirs(workspace_src)

    try:
        init_workspace(workspace_src)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(2)

