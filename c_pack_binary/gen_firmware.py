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

def create_header(binary_offset, binary_size, version_offset, version_size, 
                  reserved0_offset, reserved0_size, reserved1_offset, reserved1_size, 
                  reserved2_offset, reserved2_size, reserved3_offset, reserved3_size,
                  binary_crc, version_crc, reserved0_crc, reserved1_crc, 
                  reserved2_crc, reserved3_crc):
    """Create the header for the binary file."""
    header = struct.pack(
        '<I I I I I I I I I I I I I I I I I I I',  # Format: little-endian unsigned integers
        HEADER_MAGIC,         # Magic number
        binary_offset,        # Binary offset
        binary_size,          # Binary size
        version_offset,       # Version offset
        version_size,         # Version size
        reserved0_offset,     # Reserved0 offset
        reserved0_size,       # Reserved0 size
        reserved1_offset,     # Reserved1 offset
        reserved1_size,       # Reserved1 size
        reserved2_offset,     # Reserved2 offset
        reserved2_size,       # Reserved2 size
        reserved3_offset,     # Reserved3 offset
        reserved3_size,       # Reserved3 size
        binary_crc,           # Binary CRC
        version_crc,          # Version CRC
        reserved0_crc,        # Reserved0 CRC
        reserved1_crc,        # Reserved1 CRC
        reserved2_crc,        # Reserved2 CRC
        reserved3_crc         # Reserved3 CRC
    )
    return header

def validate_file(path):
    """Check if a file exists and is readable."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file '{path}' does not exist.")
    if not os.access(path, os.R_OK):
        raise PermissionError(f"The file '{path}' cannot be read.")

def main():
    parser = argparse.ArgumentParser(description='Package a binary file, version string, and optional reserved files into a single binary file.')
    parser.add_argument('-f', '--file', required=True, help='Path to the binary file to be packed.')
    parser.add_argument('-v', '--version', required=True, help='Version string to be included in the package.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output packed file.')
    parser.add_argument('-r0', '--reserved0', help='Path to the optional reserved0 file.')
    parser.add_argument('-r1', '--reserved1', help='Path to the optional reserved1 file.')
    parser.add_argument('-r2', '--reserved2', help='Path to the optional reserved2 file.')
    parser.add_argument('-r3', '--reserved3', help='Path to the optional reserved3 file.')
    
    args = parser.parse_args()

    try:
        # Validate input binary file
        validate_file(args.file)

        # Read binary file
        with open(args.file, 'rb') as file:
            file_data = file.read()

        binary_size = len(file_data)
        binary_crc = calculate_crc(file_data)
        binary_offset = struct.calcsize('<I I I I I I I I I I I I I I I I I I I')  # Size of the header

        # Calculate CRC for version string
        version_data = args.version.encode('utf-8')
        version_size = len(version_data)
        version_crc = calculate_crc(version_data)
        version_offset = binary_offset + binary_size

        # Process optional reserved files
        reserved_offsets = [0, 0, 0, 0]
        reserved_sizes = [0, 0, 0, 0]
        reserved_crcs = [0, 0, 0, 0]
        reserved_data = ["", "", "", ""]

        reserved_files = [args.reserved0, args.reserved1, args.reserved2, args.reserved3]

        current_offset = version_offset + version_size

        for i in range(4):
            if reserved_files[i]:
                validate_file(reserved_files[i])
                with open(reserved_files[i], 'rb') as res_file:
                    data = res_file.read()
                    reserved_sizes[i] = len(data)
                    reserved_crcs[i] = calculate_crc(data)
                    reserved_offsets[i] = current_offset
                    reserved_data[i] = data
                    current_offset += reserved_sizes[i]

        # Create header
        header = create_header(
            binary_offset, binary_size, version_offset, version_size,
            reserved_offsets[0], reserved_sizes[0], reserved_offsets[1], reserved_sizes[1],
            reserved_offsets[2], reserved_sizes[2], reserved_offsets[3], reserved_sizes[3],
            binary_crc, version_crc, reserved_crcs[0], reserved_crcs[1],
            reserved_crcs[2], reserved_crcs[3]
        )

        # Write to output file
        with open(args.output, 'wb') as output_file:
            output_file.write(header)
            output_file.write(file_data)
            output_file.write(version_data)

            for i in range(4):
                if reserved_data[i]:
                    output_file.write(reserved_data[i])

        # Print header information
        print("Header Information:")
        print(f"Magic: {hex(HEADER_MAGIC)}")
        print(f"Binary Offset: {binary_offset}")
        print(f"Binary Size: {binary_size}")
        print(f"Version Offset: {version_offset}")
        print(f"Version Size: {version_size}")
        print(f"Binary CRC: {hex(binary_crc)}")
        print(f"Version CRC: {hex(version_crc)}")

        for i in range(4):
            if reserved_files[i]:
                print(f"Reserved{i} Offset: {reserved_offsets[i]}")
                print(f"Reserved{i} Size: {reserved_sizes[i]}")
                print(f"Reserved{i} CRC: {hex(reserved_crcs[i])}")

        print('Firmware image packed successfully.')

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except PermissionError as e:
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
