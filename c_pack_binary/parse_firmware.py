import struct
import zlib
import sys
import argparse
import os

"""
Header Structure (in bytes):
+---------------------------+------------------------------+------------------------------+
| Field Name                | Size (in bytes)              | Description                  |
+---------------------------+------------------------------+------------------------------+
| Magic                     | 4                            | Magic number (0x76787a7f)    |
| Binary Offset             | 4                            | Offset to binary data        |
| Binary Size               | 4                            | Size of the binary data      |
| Version Offset            | 4                            | Offset to version string     |
| Version Size              | 4                            | Size of the version string   |
| Reserved0 Offset          | 4                            | Offset to reserved0          |
| Reserved0 Size            | 4                            | Size of reserved0            |
| Reserved1 Offset          | 4                            | Offset to reserved1          |
| Reserved1 Size            | 4                            | Size of reserved1            |
| Reserved2 Offset          | 4                            | Offset to reserved2          |
| Reserved2 Size            | 4                            | Size of reserved2            |
| Reserved3 Offset          | 4                            | Offset to reserved3          |
| Reserved3 Size            | 4                            | Size of reserved3            |
| Binary CRC                | 4                            | CRC32 checksum of binary data|
| Version CRC               | 4                            | CRC32 checksum of version    |
| Reserved0 CRC             | 4                            | CRC32 checksum of reserved0  |
| Reserved1 CRC             | 4                            | CRC32 checksum of reserved1  |
| Reserved2 CRC             | 4                            | CRC32 checksum of reserved2  |
| Reserved3 CRC             | 4                            | CRC32 checksum of reserved3  |
+---------------------------+------------------------------+------------------------------+
| Total Header Size         | 80                           | Total size of the header     |
+---------------------------+------------------------------+------------------------------+
"""

HEADER_MAGIC = 0x76787a7f

def calculate_crc(data):
    """Calculate CRC32 checksum for the given data."""
    return zlib.crc32(data)

def validate_header(header):
    """Validate the parsed header structure."""
    magic, binary_offset, binary_size, version_offset, version_size, reserved0_offset, reserved0_size, \
    reserved1_offset, reserved1_size, reserved2_offset, reserved2_size, reserved3_offset, reserved3_size, \
    binary_crc, version_crc, reserved0_crc, reserved1_crc, reserved2_crc, reserved3_crc = header
    
    if magic != HEADER_MAGIC:
        raise ValueError(f"Invalid magic number: {hex(magic)}")

def parse_firmware(input_path, binary_output_path, version_output_path, reserved_output_paths):
    with open(input_path, 'rb') as file:
        # Read and unpack the header
        header_format = '<I I I I I I I I I I I I I I I I I I I'
        header_size = struct.calcsize(header_format)
        header_data = file.read(header_size)
        header = struct.unpack(header_format, header_data)

        # Validate the header
        validate_header(header)

        # Extract header fields
        magic, binary_offset, binary_size, version_offset, version_size, reserved0_offset, reserved0_size, \
        reserved1_offset, reserved1_size, reserved2_offset, reserved2_size, reserved3_offset, reserved3_size, \
        binary_crc, version_crc, reserved0_crc, reserved1_crc, reserved2_crc, reserved3_crc = header

        # Print header information
        print("Header Information:")
        print(f"Magic: {hex(magic)}")
        print(f"Binary Offset: {binary_offset}")
        print(f"Binary Size: {binary_size}")
        print(f"Version Offset: {version_offset}")
        print(f"Version Size: {version_size}")
        print(f"Binary CRC: {hex(binary_crc)}")
        print(f"Version CRC: {hex(version_crc)}")

        for i in range(4):
            offset = [reserved0_offset, reserved1_offset, reserved2_offset, reserved3_offset][i]
            size = [reserved0_size, reserved1_size, reserved2_size, reserved3_size][i]
            crc = [reserved0_crc, reserved1_crc, reserved2_crc, reserved3_crc][i]
            if offset != 0 and size != 0:
                print(f"Reserved{i} Offset: {offset}")
                print(f"Reserved{i} Size: {size}")
                print(f"Reserved{i} CRC: {hex(crc)}")

        # Read and validate binary data
        file.seek(binary_offset)
        binary_data = file.read(binary_size)
        calculated_binary_crc = calculate_crc(binary_data)
        if calculated_binary_crc != binary_crc:
            raise ValueError("Binary CRC mismatch!")

        # Write binary data to the specified output file
        with open(binary_output_path, 'wb') as binary_output_file:
            binary_output_file.write(binary_data)
        
        print(f"Binary data extracted to: {binary_output_path}")

        # Read and validate version data
        file.seek(version_offset)
        version_data = file.read(version_size)
        calculated_version_crc = calculate_crc(version_data)
        if calculated_version_crc != version_crc:
            raise ValueError("Version CRC mismatch!")

        version_str = version_data.decode('utf-8')
        with open(version_output_path, 'w') as version_output_file:
            version_output_file.write(version_str)
        
        print(f"Version data extracted to: {version_output_path}")

        # Extract reserved sections
        for i in range(4):
            offset = [reserved0_offset, reserved1_offset, reserved2_offset, reserved3_offset][i]
            size = [reserved0_size, reserved1_size, reserved2_size, reserved3_size][i]
            crc = [reserved0_crc, reserved1_crc, reserved2_crc, reserved3_crc][i]
            if offset != 0 and size != 0:
                file.seek(offset)
                reserved_data = file.read(size)
                calculated_reserved_crc = calculate_crc(reserved_data)
                if calculated_reserved_crc != crc:
                    raise ValueError(f"Reserved{i} CRC mismatch!")

                if reserved_output_paths[i]:
                    with open(reserved_output_paths[i], 'wb') as reserved_output_file:
                        reserved_output_file.write(reserved_data)
                    print(f"Reserved{i} data extracted to: {reserved_output_paths[i]}")

def main():
    parser = argparse.ArgumentParser(description='Parse a firmware package and extract its components.')
    parser.add_argument('-f', '--file', required=True, help='Path to the firmware package file to be parsed.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output binary file.')
    parser.add_argument('-v', '--version', required=True, help='Path to the output version file.')
    parser.add_argument('-r0', '--reserved0', help='Path to the output reserved0 file.')
    parser.add_argument('-r1', '--reserved1', help='Path to the output reserved1 file.')
    parser.add_argument('-r2', '--reserved2', help='Path to the output reserved2 file.')
    parser.add_argument('-r3', '--reserved3', help='Path to the output reserved3 file.')
    
    args = parser.parse_args()

    reserved_output_paths = [args.reserved0, args.reserved1, args.reserved2, args.reserved3]

    try:
        parse_firmware(args.file, args.output, args.version, reserved_output_paths)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"IO Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
