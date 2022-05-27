from warnings import warn


def run_length_encoder(in_bytes: bytes) -> bytes:
    """Compress a series of bytes using run-length-encoding (RLE)

    RLE represents data with 2 byte pairs. The first represents the number of times
    the value will repeat, the second the value to be repeated.

    e.g.
    0, 0, 0, 0, 1, 1, 2, 0, 0 -> (4 , 0), (2, 1), (1, 2), (2, 0)


    The sequence is terminated by a final byte with value 0.

    When used for tile based data the compression can be significant.
    """
    print(f"Compressing {len(in_bytes)} bytes with run-length-encoding...")
    byte_array = [b for b in in_bytes]
    run_length_array = []
    last_value = byte_array[0]
    length = 0
    for index, byte in enumerate(byte_array):
        if (byte != last_value) or (length == 255):
            # New data sequence encountered
            # OR max storable length (256) reached
            run_length_array.append(length)
            run_length_array.append(last_value)
            last_value = byte
            length = 1
        elif index == len(byte_array) - 1:
            # Final byte in the sequence, flush results
            run_length_array.append(length + 1)
            run_length_array.append(last_value)
            # Add `x00` as terminating byte
            run_length_array.append(0)
        else:
            length += 1

    compress_bytes = bytes(run_length_array)

    compressed_byte_length = len(compress_bytes)
    original_byte_length = len(in_bytes)

    # In some circumstances compressed data can exceed original data length.
    # If this is the case the user is warned.
    if compressed_byte_length > original_byte_length:
        warn(
            "data size is larger after compression "
            f"({compressed_byte_length} vs. {original_byte_length} bytes). "
            "Consider alternate compression scheme.",
            UserWarning,
        )
    print(f"Saved {original_byte_length-compressed_byte_length} bytes in compression.")
    return compress_bytes


def run_length_decoder(compressed_bytes: bytes) -> bytes:
    """Decode a series of bytes encoded using RLE.

    See `run_length_encoder` for details.
    """
    print(f"Uncompressing {len(compressed_bytes)} bytes with run-length-encoding...")
    comp_byte_array = [b for b in compressed_bytes]
    uncomp_byte_array = []

    for i in range(0, len(comp_byte_array), 2):
        length = comp_byte_array[i]
        if length == 0:
            break
        val = comp_byte_array[i + 1]
        unpacked = [val] * length
        uncomp_byte_array.extend(unpacked)

    out_bytes = bytes(uncomp_byte_array)
    print(f"Expanded {len(out_bytes) - len(compressed_bytes)} bytes in decompression.")
    return out_bytes
