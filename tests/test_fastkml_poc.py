import pytest
import shapely  # type: ignore
from haifa_points import (INSIDE_POLYGON_GCS, INSIDE_POLYGON_UTM,
                          ON_EDGE_INSIDE_POLYGON_GCS, OUTSIDE_POLYGON_GCS,
                          OUTSIDE_POLYGON_UTM,
                          SAME_ON_EDGE_OUTSIDE_POLYGON_UTM)


@pytest.mark.parametrize("lon_lat", INSIDE_POLYGON_GCS)
def test_haifa_gcs_coordinates_in_polygon(gcs_haifa_polygon: shapely.Polygon,
                                          lon_lat: shapely.Point):
    assert gcs_haifa_polygon.contains(lon_lat)


@pytest.mark.parametrize("xy", INSIDE_POLYGON_UTM)
def test_haifa_utm_coordinates_in_polygon(utm_haifa_polygon: shapely.Polygon,
                                          xy: shapely.Point):
    assert utm_haifa_polygon.contains(xy)


@pytest.mark.parametrize("lon_lat", OUTSIDE_POLYGON_GCS)
def test_haifa_gcs_coordinates_out_of_polygon(
        gcs_haifa_polygon: shapely.Polygon, lon_lat: shapely.Point):
    assert not gcs_haifa_polygon.contains(lon_lat)


@pytest.mark.parametrize("xy", OUTSIDE_POLYGON_UTM)
def test_haifa_utm_coordinates_out_of_polygon(
        utm_haifa_polygon: shapely.Polygon, xy: shapely.Point):
    assert not utm_haifa_polygon.contains(xy)


def test_point_on_the_edge(gcs_haifa_polygon: shapely.Polygon,
                           utm_haifa_polygon: shapely.Polygon):
    gcs_point = ON_EDGE_INSIDE_POLYGON_GCS
    utm_same_point = SAME_ON_EDGE_OUTSIDE_POLYGON_UTM
    assert gcs_haifa_polygon.contains(gcs_point)
    assert not utm_haifa_polygon.contains(utm_same_point)
