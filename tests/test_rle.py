from pathlib import Path

import pytest

import rle

TEST_DATA_FOLDER = Path(__file__).parent.absolute() / "test_data"
UNCOMPR_DATA_PATH = TEST_DATA_FOLDER / "uncompressed.dat"
RLE_COMPR_DATA_PATH = TEST_DATA_FOLDER / "rle_compressed.dat"


@pytest.fixture
def uncompressed_data():
    with UNCOMPR_DATA_PATH.open("rb") as infile:
        data = infile.read()
    return data


@pytest.fixture
def rle_compressed_data():
    with RLE_COMPR_DATA_PATH.open("rb") as infile:
        data = infile.read()
    return data


def test_version():
    assert rle.__version__ == "0.1.1"


def test_run_length_encoder(uncompressed_data, rle_compressed_data):
    test_dat = rle.run_length_encoder(uncompressed_data)
    assert test_dat == rle_compressed_data, "RLE encoded data does not match control."
    assert (
        test_dat[-1] == 0
    ), f"Final byte of RLE encoded data should be 0, got {test_dat[-1]}"

    # Test that a warning if produced if compression increases data size.
    short_bytes = bytes([0, 1, 2, 3, 4])
    with pytest.warns(UserWarning):
        rle.run_length_encoder(short_bytes)


def test_run_length_decoder(uncompressed_data, rle_compressed_data):
    test_dat = rle.run_length_decoder(rle_compressed_data)
    assert test_dat == uncompressed_data, "Decoded data does not match control."


def test_open_byte_file(uncompressed_data, rle_compressed_data):
    # Test Path() based opening
    test_dat = rle.open_byte_file(UNCOMPR_DATA_PATH)
    assert test_dat == uncompressed_data, "Opened byte data does not match control."
    # Test string based opening
    test_dat = rle.open_byte_file(str(RLE_COMPR_DATA_PATH))
    assert test_dat == rle_compressed_data, "Opened byte data does not match control."
    # Test exception handling
    with pytest.raises(FileNotFoundError):
        rle.open_byte_file("./file_that_doesnt_exist.dat")


def test_save_byte_file(tmp_path, rle_compressed_data, uncompressed_data):
    test_comp_path: Path = tmp_path / "test_rle_comp.dat"
    rle.save_byte_file(rle_compressed_data, test_comp_path)
    assert test_comp_path.exists(), f"Saved file at {test_comp_path} not found."
    with test_comp_path.open("rb") as infile:
        reopened_dat = infile.read()
    assert (
        reopened_dat == rle_compressed_data
    ), "Saved file data does not match control."
