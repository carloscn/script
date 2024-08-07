# !/bin/bash
function __check_ret() {
    if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

if [ ! -d u-boot ];then
    git clone git@github.com:nxp-auto-linux/u-boot.git -b bsp36.0-2022.04
    __check_ret $? "git clone uboot"
fi

# build u-boot
pushd u-boot

echo "CONFIG_OPTEE=y" >> ./configs/s32g274ardb2_defconfig

make CROSS_COMPILE=aarch64-none-linux-gnu- s32g274ardb2_defconfig
__check_ret $? "make config"

make CROSS_COMPILE=aarch64-none-linux-gnu- -j8
__check_ret $? "make uboot"

ls -al u-boot-nodtb.bin

popd

# build OPTEE-OS

if [ ! -d optee_os ];then
    git clone git@github.com:nxp-auto-linux/optee_os.git -b bsp36.0-3.18
    __check_ret $? "git clone optee-os"
fi

pushd optee_os

make CROSS_COMPILE64=aarch64-none-linux-gnu- PLATFORM=s32 PLATFORM_FLAVOR=s32g2 -j8
__check_ret $? "make opteeos"

ls -al out/arm-plat-s32/core/tee-header_v2.bin out/arm-plat-s32/core/tee-pager_v2.bin

popd


# build TF-A

if [ ! -d arm-trusted-firmware ];then
    git clone git@github.com:nxp-auto-linux/arm-trusted-firmware.git -b bsp36.0-2.5
    __check_ret $? "git clone tfa"
fi

pushd arm-trusted-firmware

make CROSS_COMPILE=aarch64-none-linux-gnu- \
     ARCH=aarch64 PLAT=s32g274ardb2 \
     BL33=`pwd`/../u-boot/u-boot-nodtb.bin \
     BL32=`pwd`/../optee_os/out/arm-plat-s32/core/tee-header_v2.bin \
     BL32_EXTRA1=`pwd`/../optee_os/out/arm-plat-s32/core/tee-pager_v2.bin \
     SPD=opteed -j8
__check_ret $? "make arm-trusted-firmware"

# sudo dd if=`pwd`/build/s32g2xxaevb/release/fip_no_ivt.s32 \
#         of=/dev/sda \
#         conv=notrunc,fsync seek=0 bs=256 count=1 && sync && \
# sudo dd if=`pwd`/build/s32g2xxaevb/release/fip.s32 \
#         of=/dev/sda \
#         conv=notrunc,fsync seek=1 bs=512 skip=1 && sync
# __check_ret $? "burn sd card"

popd

if [ ! -d linux ];then
    git clone git@github.com:nxp-auto-linux/linux.git -b bsp36.0-5.15.85-rt
    __check_ret $? "git clone linux"
fi

pushd linux

echo "ONFIG_TEE=y" >> arch/arm64/configs/s32cc_defconfig
echo "CONFIG_OPTEE=y" >> arch/arm64/configs/s32cc_defconfig
echo "CONFIG_OPTEE_SHM_NUM_PRIV_PAGES=256" >> arch/arm64/configs/s32cc_defconfig
echo "CONFIG_HAVE_ARM_SMCCC=y" >> arch/arm64/configs/s32cc_defconfig

make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- s32cc_defconfig
__check_ret $? "make linux config"

make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- -j16
__check_ret $? "make linux"

ls -al `pwd`/arch/arm64/boot/Image `pwd`/arm64/boot/dts/freescale/s32g2xxa-evb.dtb

popd