#include <QFile>
#include <QDataStream>
#include <QByteArray>
#include <QCryptographicHash>
#include <QFileInfo>
#include <QtEndian>


/*
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
*/

#define HEADER_MAGIC 0x76787a7f

qint32 MainWindow::parseImageFile(QString image_path, QString out_binary, QString &version, 
                                  QString out_reserved0, QString out_reserved1, 
                                  QString out_reserved2, QString out_reserved3) {
    QFile inputFile(image_path);
    if (!inputFile.open(QIODevice::ReadOnly)) {
        return -1;  // Error: unable to open input file
    }

    QDataStream in(&inputFile);
    in.setByteOrder(QDataStream::LittleEndian);

    // Read and validate the header
    quint32 magic;
    quint32 binary_offset, binary_size, version_offset, version_size;
    quint32 reserved0_offset, reserved0_size, reserved1_offset, reserved1_size;
    quint32 reserved2_offset, reserved2_size, reserved3_offset, reserved3_size;
    quint32 binary_crc, version_crc, reserved0_crc, reserved1_crc;
    quint32 reserved2_crc, reserved3_crc;

    in >> magic
       >> binary_offset >> binary_size >> version_offset >> version_size
       >> reserved0_offset >> reserved0_size >> reserved1_offset >> reserved1_size
       >> reserved2_offset >> reserved2_size >> reserved3_offset >> reserved3_size
       >> binary_crc >> version_crc >> reserved0_crc >> reserved1_crc
       >> reserved2_crc >> reserved3_crc;

    if (magic != HEADER_MAGIC) {
        return -2;  // Error: invalid magic number
    }

    // Read and validate binary data
    inputFile.seek(binary_offset);
    QByteArray binaryData = inputFile.read(binary_size);
    quint32 calculated_binary_crc = qChecksum(binaryData.constData(), binaryData.size());

    if (calculated_binary_crc != binary_crc) {
        return -3;  // Error: binary CRC mismatch
    }

    // Write binary data to the specified output file
    QFile outputFile(out_binary);
    if (!outputFile.open(QIODevice::WriteOnly)) {
        return -4;  // Error: unable to open output file
    }
    outputFile.write(binaryData);
    outputFile.close();

    // Read and validate version data
    inputFile.seek(version_offset);
    QByteArray versionData = inputFile.read(version_size);
    quint32 calculated_version_crc = qChecksum(versionData.constData(), versionData.size());

    if (calculated_version_crc != version_crc) {
        return -5;  // Error: version CRC mismatch
    }

    version = QString::fromUtf8(versionData);

    // Process reserved sections
    struct ReservedSection {
        quint32 offset;
        quint32 size;
        quint32 crc;
        QString outputPath;
    };

    ReservedSection reservedSections[4] = {
        {reserved0_offset, reserved0_size, reserved0_crc, out_reserved0},
        {reserved1_offset, reserved1_size, reserved1_crc, out_reserved1},
        {reserved2_offset, reserved2_size, reserved2_crc, out_reserved2},
        {reserved3_offset, reserved3_size, reserved3_crc, out_reserved3}
    };

    for (int i = 0; i < 4; i++) {
        if (reservedSections[i].offset != 0 && reservedSections[i].size != 0) {
            inputFile.seek(reservedSections[i].offset);
            QByteArray reservedData = inputFile.read(reservedSections[i].size);
            quint32 calculated_reserved_crc = qChecksum(reservedData.constData(), reservedSections[i].size);

            if (calculated_reserved_crc != reservedSections[i].crc) {
                return -6 - i;  // Error: reserved CRC mismatch (specific to section)
            }

            if (!reservedSections[i].outputPath.isEmpty()) {
                QFile reservedOutputFile(reservedSections[i].outputPath);
                if (!reservedOutputFile.open(QIODevice::WriteOnly)) {
                    return -10 - i;  // Error: unable to open reserved output file (specific to section)
                }
                reservedOutputFile.write(reservedData);
                reservedOutputFile.close();
            }
        }
    }

    return 0;  // Success
}

QString version;
qint32 result = parseImageFile("output.pack.bin", "TC377_TX.hex", version, 
                               "reserved0_out.bin", "reserved1_out.bin", 
                               "reserved2_out.bin", "reserved3_out.bin");

if (result == 0) {
    qDebug() << "Parsing successful!";
    qDebug() << "Extracted version:" << version;
} else {
    qDebug() << "Parsing failed with error code:" << result;
}