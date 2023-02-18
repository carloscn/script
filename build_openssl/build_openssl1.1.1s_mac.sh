#!/bin/bash

function __utils_check_ret() {
    if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

target_ball=openssl-1.1.1s.tar.gz
target_path=openssl-1.1.1s

if [ ! -f ${target_ball} ];then
    aria2c -x5 "https://github.com/openssl/openssl/releases/download/OpenSSL_1_1_1s/openssl-1.1.1s.tar.gz"
    __utils_check_ret $? "download failed!"
fi

tar -zxvf ${target_ball}
cd ${target_path}
__utils_check_ret $? "tar -zxvf failed!"

./Configure darwin64-x86_64-cc no-asm --prefix=`pwd`/out
__utils_check_ret $? "config failed!"

make `nproc`

make install

ls ./out
