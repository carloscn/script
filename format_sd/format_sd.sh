# !/bin/bash

echo "[INFO] Clear the SD card"
dd if=/dev/zero of=/dev/${1} bs=4k count=1
parted /dev/${1} mklabel gpt
echo "[INFO] parted boot partition"
parted /dev/${1} --script mkpart primary fat32 0% 1G
echo "[INFO] parted rootfs partition"
parted /dev/${1} --script mkpart primary ext4 1G 100%
echo "[INFO] print partitions"
parted /dev/${1} print
echo "[INFO] mkfs vfat on boot"
mkfs.vfat /dev/${1}1
echo "[INFO] mkfs rootfs on boot"
mkfs.ext4 -F /dev/${1}2
