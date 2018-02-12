#!/usr/bin/env python3
"""
This module maintains the cli arguments
"""

import sys
import argparse


def cli_args():
    """
    Process cli arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--schedule", help="create scheduled execution",
                        action="store_true")
    parser.add_argument("-c", "--cancel", help="cancel scheduled execution",
                        action="store_true")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()
