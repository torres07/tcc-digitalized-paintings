#bin/bash

cd ../sample_damicore;

a=1
for i in *; do
  new=$(printf "%d_s.txt" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done
