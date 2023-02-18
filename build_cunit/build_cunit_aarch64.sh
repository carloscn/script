#!/bin/bash

CROSS_COMPILE=aarch64-linux-gnu-gcc
HOST=aarch64-linux-gnu

function __utils_check_ret() {

    if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

target_ball=CUnit-2.1-3.tar.bz2
target_path=CUnit-2.1-3

if [ ! -f ${target_ball} ];then
    aria2c -x5 "https://github.com/carloscn/CUnit/releases/download/CUnit-2.1-3/CUnit-2.1-3.tar.bz2"
    __utils_check_ret $? "download CUnit failed!"
fi

tar -xvf ${target_ball}
__utils_check_ret $? "tar -xvf failed!"

cd ${target_path}

aclocal
autoconf
autoreconf -i
automake
automake --add-missing

CC=${CROSS_COMPILE} ./configure --prefix=`pwd`/out --host=${HOST}

make -j8

make install

tree ./out
