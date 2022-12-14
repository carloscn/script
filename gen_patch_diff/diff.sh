#! /bin/bash

rm -rf *.patch
diff -Nu ${1} ${2} >> ${1}.patch

TEMP_DIR=temp_${RANDOM}
mkdir -p ${TEMP_DIR}

mv ${2} ${TEMP_DIR} > /dev/null

ls -al *.patch

