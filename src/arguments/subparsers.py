import argparse
import tempfile


def train(subparsers) -> None:
    subparser = subparsers.add_parser(
        "train",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    
    subparser.add_argument(
        "--batch",
        help="Add help to your subparser's argument",
    )

    subparser.add_argument(
        "--arg1",
        help="Add help to your subparser's argument",
    )


def test(subparsers) -> None:
    subparser = subparsers.add_parser(
        "test",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    
    subparser.add_argument(
        "--batch",
        help="Add help to your subparser's argument",
    )

    subparser.add_argument(
        "--arg2",
        help="Add help to your subparser's argument",
    )


