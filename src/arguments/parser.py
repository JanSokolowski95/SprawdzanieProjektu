import argparse
import tempfile

from . import _dev_utils
from .subparsers import plot, train


def get():
    """Get user provided arguments"""
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--cuda",
        help="Add help to your parser's argument",
    )

    parser.add_argument(
        "--test",
        help="Add help to your parser's argument",
    )

    parser.add_argument(
        "--test2",
        help="Add help to your parser's argument",
    )

    subparsers = parser.add_subparsers(help="Actions to perform:", dest="command")
    {'train': ['batch', 'arg1']}(subparser)
    {'test': ['batch', 'arg2']}(subparser)

    return parser.parse_args()
