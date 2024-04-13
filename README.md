# py-static-dtm
This is a package for creating custom static DTMs using polygons to define the DTM geographic area.

The main packages here are: fastkml and shapely. pyproj is only used here to convert the coordinates to UTM.

One key feature is the ability to create a DTM out of a kml file. For creating a kml file easily you can tap into [google earth](https://earth.google.com/web/) and export the kml you sketched.

## The tests
The tests use a set of points to assert the behavior against a kml file of Haifa port. You can load the kml into [google earth](https://earth.google.com/web/) to see the polygon.

In the docs folder there is another kml file. Loading it to google earth will show on top of the polygon all the points the tests are checking. This file was manually created, if the tests will change, the file may loose its validity.
