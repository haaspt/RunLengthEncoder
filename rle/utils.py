from pathlib import Path
from typing import Union


def open_byte_file(filename: Union[str, Path]) -> bytes:
    file = Path(filename)
    if not file.exists():
        raise FileNotFoundError(f"File at {file.absolute} not found.")
    with open(file, "rb") as f:
        byte_data = f.read()
    return byte_data


def save_byte_file(out_bytes: bytes, filename: Union[str, Path] = "out.dat"):
    with open(filename, "wb") as f:
        f.write(out_bytes)
    print(f"Wrote bytes to {filename}.")


def print_bytes(byte_array: bytes, sep: str = "-"):
    print(byte_array.hex(sep))
