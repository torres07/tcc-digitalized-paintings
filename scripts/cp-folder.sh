#bin/bash

N=512;
srcdir=religious-painting/images;
dstdir=fullbase1;
for i in "${srcdir}"/*; do
  [ "$((N--))" = 0 ] && break
  cp -t "${dstdir}" -- "$i"
done
