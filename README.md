Readme
======
GB Leisure is a CartoCSS style intended for use with OpenStreetMap data, OS OpenData Terrain 50 contour shapefiles and Charles Roper's OSGB 1km grid shapefile (https://github.com/charlesroper/OSGB_Grids).

The style is very much a work in progress and is missing a number of important features. The aim is to produce a map style that can be used for hiking etc. in Great Britain that shows relevant features (including public rights of way defined in the OpenStreetMap database by the designation tag) and uses the OSGB projection and grid (EPSG:27700).

Files
-----
- The project.mml and style.mss files were created using TileMill
- The generate-xml.sh BASH script uses carto to generate a Mapnik XML file and sed to replace the TileMill default projection with the OSGB one
- The print-osgb.py Python script uses Mapnik to render a map which uses the OSGB projection using a given paper size, scale and origin (specified using an OSGB numerical grid reference). It could also be used to render alternative Mapnik styles in a similar fashion

Licence
-------
Feel free to use this code in your own projects (see LICENCE file for details) but please provide attribution and (where possible) a link to https://github.com/gregrs-uk/gb-leisure-carto/ in your code and alongside any map renders.
