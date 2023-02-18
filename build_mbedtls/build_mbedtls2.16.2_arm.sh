#!/bin/bash

CROSS_COMPILE=arm-linux-gnueabihf-gcc

function __utils_check_ret() {
    if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

target_ball=mbedtls-2.16.4.tar.gz
target_path=mbedtls-2.16.4

if [ ! -f ${target_ball} ];then
    aria2c -x5 "https://github.com/Mbed-TLS/mbedtls/archive/refs/tags/mbedtls-2.16.4.tar.gz" -o ${target_ball}
    __utils_check_ret $? "download failed!"
fi

tar -zxvf ${target_ball}
cd mbedtls-mbedtls-2.16.4
__utils_check_ret $? "tar -zxvf failed!"

cmake -DUSE_SHARED_MBEDTLS_LIBRARY:Bool=ON \
      -DENABLE_TESTING:Bool=OFF \
      -DENABLE_PROGRAMS:Bool=ON \
      -DCMAKE_C_COMPILER=${CROSS_COMPILE} \
      -DCMAKE_INSTALL_PREFIX="./out"

make install DESTDIR=`pwd`/out
