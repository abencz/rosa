#!/usr/bin/env python
# -*- coding: ascii -*-

from os import path
import re


def confirm_workspace(workspace_path):
    # we should expect to find a CMakeLists.txt file here
    cmake_path = path.join(workspace_path, 'src', 'CMakeLists.txt')
    if not path.isfile(cmake_path):
        return False

    with file(cmake_path, 'r') as f:
        # try to find magical catkin_workspace() indication from the workspace
        # CMakeLists.txt file
        lines = [line for line in f.readlines() if re.match('^catkin_workspace()', line)]

    if len(lines) < 1:
        return False

    return True


def find_workspace(starting_path):
    current_path = path.abspath(starting_path)

    while current_path != path.sep:
        if confirm_workspace(current_path):
            return current_path

        current_path = path.dirname(current_path)

    return None
