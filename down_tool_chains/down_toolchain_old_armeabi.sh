#!/bin/bash

# From https://releases.linaro.org/components/toolchain/binaries/

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

#CROSS_AEBI_ADDR="https://releases.linaro.org/components/toolchain/binaries/7.5-2019.12/arm-eabi/gcc-linaro-7.5.0-2019.12-x86_64_arm-eabi.tar.xz"
CROSS_AEBI_ADDR="https://mirrors.tuna.tsinghua.edu.cn/armbian-releases/_toolchain/gcc-linaro-7.4.1-2019.02-x86_64_arm-eabi.tar.xz"

utils_wget_download ${CROSS_AEBI_ADDR} || utils_check_ret $? "wget the ARM cross compiler toolchains"

DEST_DIR=/opt/cross-compile
sudo mkdir -p ${DEST_DIR} || utils_check_ret $? "touch dir failed"

FILE=$(basename "$CROSS_AEBI_ADDR")
sudo tar -xvf ${FILE} -C ${DEST_DIR} || utils_check_ret $? "install eabi"
