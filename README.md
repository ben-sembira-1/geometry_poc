# geometry_poc
This is a poc for using polygons to assert if a point is in a certain area.

The main packages here are: fastkml and shapely. pyproj is only used here to convert the coordinates to UTM.

## The tests
The tests use a custom kml (in the tests folder) with a polygon of Haifa sea, you can load the kml into [google earth](https://earth.google.com/web/) to see the polygon.

In the docs folder there is another kml file. Loading it to google earth will show on top of the polygon all the points the tests are checking.
