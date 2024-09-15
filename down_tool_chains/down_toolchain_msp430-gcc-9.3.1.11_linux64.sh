#!/bin/bash

# From https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads

function utils_wget_download()
{
    URL=$1
    FILE=$(basename "$URL")

    if [ -f "$FILE" ]; then
        echo "$FILE already exists. Checking if it is complete..."

        if tar -tf "$FILE" &> /dev/null; then
            echo "$FILE is complete. Skipping download."
            return 0
        else
            echo "$FILE is incomplete. Deleting and re-downloading."
            rm "$FILE"
        fi
    fi

    echo "Downloading $FILE..."
    wget "$URL" -O "$FILE" --no-check-certificate

    if tar -tf "$FILE" &> /dev/null; then
        echo "$FILE downloaded and verified successfully."
    else
        echo "Failed to download a complete $FILE. Please try again."
        rm "$FILE"
        return 1
    fi
}

function utils_check_ret()
{
	if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

CROSS_MSP430_ADDR="https://dr-download.ti.com/software-development/ide-configuration-compiler-or-debugger/MD-LlCjWuAbzH/9.3.1.2/msp430-gcc-9.3.1.11_linux64.tar.bz2"

utils_wget_download ${CROSS_MSP430_ADDR} || utils_check_ret $? "wget the msp430 cross compiler toolchains"

DEST_DIR=/opt/cross-compile
sudo mkdir -p ${DEST_DIR} || utils_check_ret $? "touch dir failed"

FILE=$(basename "$CROSS_MSP430_ADDR")
sudo tar -xvjf ${FILE} -C ${DEST_DIR} || utils_check_ret $? "install eabi"
