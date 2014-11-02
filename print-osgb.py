#!/usr/bin/env python

# Script to output an OSGB map using a
# given paper size, scale and origin

# Mapnik XML file should specify srs="+init=epsg:27700"
# i.e. OSGB so that co-ordinate units are metres

import mapnik

# set some paths
stylesheet = 'gb-leisure.xml'
image = 'gb-leisure.png'

# set geometry options
left_E = 363500 # set to OSGB Easting of left edge
bottom_N = 254000 # set to OSGB Northing of bottom edge
paper_width = 0.21 # set paper width in metres, A4 = 0.210
paper_height = 0.21 # set paper height in metres, A4 = 0.297
margin = 0.01 # set margin in metres e.g. 0.01m = 1cm
scale = 25000 # set scale e.g. 25000

# set output resolution (mapnik default is 90.71)
resolution = 90.71 # change to desired output resolution e.g. 300

# ----- SET OPTIONS ABOVE THIS LINE -----

# calculate the bounding box
map_width = paper_width-(2*margin) # width of map content in metres
map_height = paper_height-(2*margin) # height of map content in metres
real_width = map_width*scale # real width of area in metres
real_height = map_height*scale # real height of area in metres
right_E = left_E + real_width # Easting of right edge
top_N = bottom_N + real_height # Northing of top edge

# mapnik's assumed pixel size and resolution
mapnik_px_size = 0.00028
inch = 0.0254 # 1 inch in metres
mapnik_resolution = inch / mapnik_px_size

# calculate the size in whole pixels and scale factor
map_width_px = int(round((resolution/inch)*map_width))
map_height_px = int(round((resolution/inch)*map_height))
scale_factor = resolution / mapnik_resolution

# make the map
m = mapnik.Map(map_width_px,map_height_px)
mapnik.load_map(m, stylesheet)
m.zoom_to_box(mapnik.Box2d(left_E,bottom_N,right_E,top_N))

print "Envelope: %s\n" % m.envelope()
print "Mapnik scale: %f" % m.scale()
print "= 1 in %f\n" % m.scale_denominator()

mapnik.render_to_file(m, image, "png", scale_factor)
print "Rendered map to image file\n"
