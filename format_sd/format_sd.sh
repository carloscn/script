# !/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: bash format_sd.sh sda"
    exit -1
fi

FILE="/dev/$1"

echo "[INFO] Clear the SD card"
dd if=/dev/zero of=${FILE} bs=4k count=100
if [ $? -eq 0 ]; then
    echo "[INFO] Clear the SD card done!"
else
    echo "[ERR] Clear the SD card"
    exit -1
fi

echo "[INFO] parted ${FILE} mklabel gpt"
parted ${FILE} mklabel gpt
if [ $? -eq 0 ]; then
    echo "[INFO] parted make label gpt done!"
else
    echo "[ERR] parted make label gpt!"
    exit -1
fi

echo "[INFO] parted boot partition"
parted ${FILE} --script mkpart primary fat32 0% 1G
if [ $? -eq 0 ]; then
    echo "[INFO] parted ${FILE} --script mkpart primary fat32 0% 1G done!"
else
    echo "[ERR] failed on parted ${FILE} --script mkpart primary fat32 0% 1G"
    exit -1
fi

echo "[INFO] parted rootfs partition"
parted ${FILE} --script mkpart primary ext4 1G 100%
if [ $? -eq 0 ]; then
    echo "[INFO] parted ${FILE} --script mkpart primary ext4 1G 100% done!"
else
    echo "[ERR] failed on parted ${FILE} --script mkpart primary ext4 1G 100%"
    exit -1
fi

echo "[INFO] print partitions"
parted ${FILE} print

echo "[INFO] mkfs vfat on boot"
mkfs.vfat ${FILE}1
if [ $? -eq 0 ]; then
    echo "[INFO] mkfs.vfat ${FILE}1 done!"
else
    echo "[ERR] failed on mkfs.vfat ${FILE}1"
    exit -1
fi

echo "[INFO] mkfs rootfs on boot"
mkfs.ext4 -F ${FILE}2
if [ $? -eq 0 ]; then
    echo "[INFO] mkfs.ext4 -F ${FILE}2 done!"
else
    echo "[ERR] failed on mkfs.ext4 -F ${FILE}2"
    exit -1
fi
echo "[INFO] format ${FILE} done!"