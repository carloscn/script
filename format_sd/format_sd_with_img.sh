# !/bin/bash

# ${1} = /dev/sdX
# ${2} = provision.elf path
# ${3} = rootfs.tar.gz path

sd=${1}
# gen the coping sd layout file by "sudo sfdisk -d /dev/sde > fdisk.layout"
# make img file: 7948206080 = 7.5G you can use 700M or 7.85G as parameter
rm -rf part.img
fallocate -l 7948206080 part.img
if [ $? -eq 0 ]; then
    echo "[INFO] fallocate -l 7948206080 part.img done!"
else
    echo "[ERR] failed on fallocate -l 7948206080 part.img"
    exit -1
fi

# use layout
sfdisk part.img < fdisk.layout
if [ $? -eq 0 ]; then
    echo "[INFO] sfdisk part.img < fdisk.layout done!"
else
    echo "[ERR] failed on sfdisk part.img < fdisk.layout"
    exit -1
fi

mockdev=`losetup --partscan --show --find part.img`
echo "[INFO] gen the ${mockdev}"

mkfs.fat -F32 ${mockdev}p1
if [ $? -eq 0 ]; then
    echo "[INFO] mkfs.fat -F32 ${mockdev}p1 done!"
else
    echo "[ERR] failed on mkfs.fat -F32 ${mockdev}p1"
    exit -1
fi

mkfs.ext4 ${mockdev}p2
if [ $? -eq 0 ]; then
    echo "[INFO] mkfs.ext4 ${mockdev}p2 done!"
else
    echo "[ERR] mkfs.ext4 ${mockdev}p2"
    exit -1
fi

random=${RANDOM}
bootpart=boot_${random}
rootfspart=rootfs_${random}
mkdir -p ${bootpart} ${rootfspart}

mount ${mockdev}p1 ${bootpart}
if [ $? -eq 0 ]; then
    echo "[INFO] mount ${mockdev}p1 ${bootpart} done!"
else
    echo "[ERR] failed on mount ${mockdev}p1 ${bootpart}"
    exit -1
fi

mount ${mockdev}p2 ${rootfspart}
if [ $? -eq 0 ]; then
    echo "[INFO] mount ${mockdev}p2 ${rootfspart} done!"
else
    echo "[ERR] failed on mount ${mockdev}p2 ${rootfspart}"
    exit -1
fi

cp -r ${2} ${bootpart}
if [ $? -eq 0 ]; then
    echo "[INFO] cp -r ${2} ${bootpart} done!"
else
    echo "[ERR] failed on cp -r ${2} ${bootpart}"
    exit -1
fi

tar -xvf ${3} -C ${rootfspart}
if [ $? -eq 0 ]; then
    echo "[INFO] tar -xvf ${3} ${rootfspart} done!"
else
    echo "[WARN] has error on tar -xvf ${3} ${rootfspart}"
fi

sync

umount ${bootpart}
if [ $? -eq 0 ]; then
    echo "[INFO] umount ${bootpart} done!"
else
    echo "[ERR] failed on umount ${bootpart}"
    exit -1
fi

umount ${rootfspart}
if [ $? -eq 0 ]; then
    echo "[INFO] umount ${rootfspart} done!"
else
    echo "[ERR] failed on umount ${rootfspart}"
    exit -1
fi

rm -rf ${bootpart} ${rootfspart}

losetup -d ${mockdev}
if [ $? -eq 0 ]; then
    echo "[INFO] losetup -d ${mockdev} done!"
else
    echo "[ERR] failed on losetup -d ${mockdev}"
    exit -1
fi

echo "[INFO] Execute dd if=./part.img of=${sd} bs=4K status=progress"
#dd if=part.img of=${sd} bs=4K status=progress
if [ $? -eq 0 ]; then
    echo "[INFO] dd if=part.img of=${sd} bs=4K status=progress done!"
else
    echo "[ERR] failed on  dd if=part.img of=${sd} bs=4K status=progress"
    exit -1
fi

echo "[INFO] done"