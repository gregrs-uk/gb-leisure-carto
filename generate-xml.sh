#!/bin/bash

# https://github.com/gregrs-uk/gb-leisure-carto/

if [ -f gb-leisure.xml ]
then
mv gb-leisure.xml gb-leisure-old.xml
fi

echo "Generating gb-leisure.xml from project.mml"
carto project.mml > gb-leisure.xml &&
if [ -f gb-leisure-old.xml ]
then
rm gb-leisure-old.xml
fi

echo "Replacing SRS with OSGB one"
sed -i 's/srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over"/srs="+init=epsg:27700"/g' gb-leisure.xml &&
echo "Done"
