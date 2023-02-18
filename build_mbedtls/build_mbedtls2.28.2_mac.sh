#!/bin/bash

function __utils_check_ret() {
    if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

target_ball=mbedtls-2.28.2.tar.gz
target_path=mbedtls-2.28.2

if [ ! -f ${target_ball} ];then
    aria2c -x5 "https://github.com/Mbed-TLS/mbedtls/archive/refs/tags/v2.28.2.tar.gz" -o ${target_ball}
    __utils_check_ret $? "download failed!"
fi

tar -zxvf ${target_ball}
cd ${target_path}
__utils_check_ret $? "tar -zxvf failed!"

cmake .
cmake -DUSE_SHARED_MBEDTLS_LIBRARY=On \
      -DCMAKE_INSTALL_PREFIX="./out" .

make -j`nproc`

echo "if you want to makeinstall in your /usr/local/ path, input the root password!"
make install
