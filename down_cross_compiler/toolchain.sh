#!/bin/bash

# https://review.spdk.io/gerrit/plugins/gitiles/spdk/spdk/+/refs/heads/master/scripts/arm_cross_compile.sh

ROOT_DIR=$(readlink -f $(dirname $0))/..
CROSS_REMOTE_ADDR="https://developer.arm.com/-/media/Files/downloads/gnu-a/10.2-2020.11/binrel/gcc-arm-10.2-2020.11-x86_64-aarch64-none-linux-gnu.tar.xz"
CROSS_NAME="gcc-arm-10.2-2020.11-x86_64-aarch64-none-linux-gnu"
CROSS_TAR_NAME="${CROSS_NAME}.tar.xz"
CROSS_DEST_DIR="${ROOT_DIR}/toolchain"

function __utils_check_ret() {
	if [ $1 -eq 0 ]; then
        echo "[INFO] $2 done!"
    else
        echo "[ERR] Failed on $2!"
        exit -1
    fi
}

function download_cc() {
    wget ${CROSS_REMOTE_ADDR} --no-check-certificate
    __utils_check_ret $? "wget the ARM cross compiler toolchains"
}

# Get Toolchain
function get_cc_toolchain() {
    ${ROOT_DIR}/toolchain/${CROSS_NAME}/bin/aarch64-none-linux-gnu-gcc -v
	if [ $1 -eq 0 ]; then
        echo "[INFO] toolchain exists!"
    else
        if [ ! -f "${CROSS_TAR_NAME}" ]; then
            echo "[INFO] cross tar file ${CROSS_TAR_NAME} does not exist!"
    		echo "[INFO] Getting ARM Cross Compiler Toolchain from the remote..."
            download_cc
        else
            echo "[INFO] toolchain tarball already exist!"
        	if [ $? -eq 0 ]; then
                echo "[INFO] test ${CROSS_TAR_NAME} done!"
            else
                echo "[INFO] the ${CROSS_TAR_NAME} is broken, download it!"
                download_cc
            fi

            # touch dir to store the toolchain
            mkdir -p ${CROSS_DEST_DIR}
    		tar -xvf ${CROSS_TAR_NAME} -C ${CROSS_DEST_DIR}

            # test cross gcc
    		$${CROSS_DEST_DIR}/${CROSS_NAME}/bin/aarch64-none-linux-gnu-gcc -v
    		__utils_check_ret $? "test cross gcc"
        fi
    fi
}

get_cc_toolchain
