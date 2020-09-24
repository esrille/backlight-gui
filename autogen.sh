#!/bin/sh
set -e
set -x

aclocal
autopoint
autoconf
automake --add-missing --copy
./configure "$@"
