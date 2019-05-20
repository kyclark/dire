"""Python equivalents of Perl's warn and die functions"""

import sys

def warn(msg):
    """Print a message to sys.stderr"""
    if msg: print(msg, file=sys.stderr)


def die(msg, exit_val=1):
    """warn() and sys.exit() with exit_val (default 1)"""
    warn(msg)
    sys.exit(exit_val)
