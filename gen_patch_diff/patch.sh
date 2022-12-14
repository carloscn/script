#! /bin/bash

patch -p0 < ${1}

mv example.txt example_changed.txt
