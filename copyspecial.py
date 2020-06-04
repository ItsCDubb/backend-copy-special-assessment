#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "???"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    path_list = [
        os.path.abspath(os.path.join(os.getcwd(), f))
        for f in (os.listdir(dirname))
        if re.search(r'__(\w+)__', f)
        ]
    return path_list


def copy_to(path_list, dest_dir):
    print('copy_to fired:', path_list, dest_dir)
    return


def zip_to(path_list, dest_zip):
    print('zip_to fired:', path_list, dest_zip)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='directory to search for files')
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
    sys.exit(1)
    if ns.todir:
        copy_to(get_special_paths(ns.from_dir), ns.todir)
    elif ns.tozip:
        zip_to(get_special_paths(ns.from_dir), ns.tozip)
    else:
        path_list = get_special_paths(ns.from_dir)
        for path in path_list:
            print(path)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
