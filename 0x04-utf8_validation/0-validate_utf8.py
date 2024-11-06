#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    """ Number of continuation bytes we are expecting"""
    num_continuation_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        """Check only the 8 least significant bits"""
        byte = byte & 0xFF

        if num_continuation_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_continuation_bytes = 3
            elif (byte >> 7):  # 1-byte character (0xxxxxxx)
                # Invalid if the highest bit is 1 in a single byte character
                return False
        else:
            # Check continuation byte (must be 10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_continuation_bytes -= 1

    return num_continuation_bytes == 0
