import argparse
from pathlib import Path

from ._version import __version__
from .encoding import run_length_decoder, run_length_encoder
from .utils import open_byte_file, print_bytes, save_byte_file


def _init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run length encoding and decoding for binary data."
    )
    parser.add_argument("filename", help="Location of bytes to operate on")
    parser.add_argument(
        "-e",
        "--encode",
        action="store_true",
        default=True,
        help="Operate in encoder mode",
    )
    parser.add_argument(
        "-d",
        "--decode",
        action="store_true",
        default=False,
        help="Operate in decoder mode",
    )
    parser.add_argument(
        "-o", "--outfile", default=None, help="Filename to save output to"
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s " + __version__,
    )

    return parser


def main():
    parser = _init_argparse()
    args = parser.parse_args()
    infile = Path(args.filename)
    b = open_byte_file(infile)
    if args.decode:
        out_b = run_length_decoder(b)
    else:
        out_b = run_length_encoder(b)
    if args.outfile:
        outfile = Path(args.outfile)
        save_byte_file(out_b, outfile)
    else:
        print_bytes(out_b)


if __name__ == "__main__":
    main()
