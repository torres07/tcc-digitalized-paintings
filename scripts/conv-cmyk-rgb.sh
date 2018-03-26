for f in ./*.jpg
  do
  type=$(identify -format '%[colorspace]' ./$f);
  #echo $type
  if [ "$type" == "CMYK" ]
  then
  echo '$f is CMYK type'
  convert ./$f -colorspace CMYK ./$
  #else
  #echo 'no work'
  fi
  done