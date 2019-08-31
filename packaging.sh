#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

rm -r $SCRIPT_DIR/build/
rm -r $SCRIPT_DIR/dist/
rm -r $SCRIPT_DIR/girepo.egg-info/

sleep 2

python $SCRIPT_DIR/setup.py sdist bdist_wheel