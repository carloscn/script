#!/bin/bash

CROSS_COMPILE=arm-linux-gnueabihf-gcc
HOST=arm-linux-gnueabihf-

function __utils_check_ret() {
    if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

target_ball=openssl-1.0.2s.tar.gz
target_path=openssl-1.0.2s

if [ ! -f ${target_ball} ];then
    aria2c -x5 "https://ftp.openssl.org/source/old/1.0.2/openssl-1.0.2s.tar.gz"
    __utils_check_ret $? "download failed!"
fi

tar -zxvf ${target_ball}
cd ${target_path}
__utils_check_ret $? "tar -zxvf failed!"

./Configure linux-armv4 no-asm shared --cross-compile-prefix=${HOST}  --prefix=`pwd`/out

make -j`nproc`
__utils_check_ret $? "make failed!"

make install

ls ./out
