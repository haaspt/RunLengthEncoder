# RLE: Run-Length Encoder

RLE is a simple utility for [run-length encoding/decoding](https://en.wikipedia.org/wiki/Run-length_encoding) of NES [tile data](https://www.nesdev.org/wiki/Tile_compression). Run-length encoding is a lossless compression format well suited for data with repetitive sequences of the same data, e.g. the tile-based background data of an 8-bit videogame.

RLE works by converting a sequence of bytes into pairs of bytes representing the byte value and the number of times it repeats. For example:

```text
Uncompressed data:
0000110220000

RLE encoded:
4021102240 -> 4*'0', 2*'1', 1*'0', 2*'2', 4*'0'
```

Compression can be very signifiant for very repetivive tile data.

## Install

Install from github:

```bash
pip install git+https://github.com/haaspt/RunLengthEncoder.git
```

Install from source:

```bash
git clone git@github.com:haaspt/RunLengthEncoder.git
cd RunLengthEncoder
poetry install
```

## Usage

```text
usage: rle [-h] [-e] [-d] [-o OUTFILE] filename

Run length encoding and decoding for binary data.

positional arguments:
  filename              Location of bytes to operate on

optional arguments:
  -h, --help            show this help message and exit
  -e, --encode          Operate in encoder mode
  -d, --decode          Operate in decoder mode
  -o OUTFILE, --outfile OUTFILE
                        Filename to save output to
```
