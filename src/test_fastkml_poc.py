import pytest
from pathlib import Path
from fastkml import kml  # type: ignore
from fastkml_poc import gcs_polygon_from_kml, gcs_polygon_to_utm_polygon
import shapely  # type: ignore


@pytest.fixture
def haifa_kml() -> kml.KML:
    haifa_kml = kml.KML()
    haifa_kml.from_string(Path("./HaifaSea.kml").read_bytes())
    return haifa_kml


@pytest.fixture
def gcs_haifa_polygon(haifa_kml: kml.KML) -> shapely.Polygon:
    return gcs_polygon_from_kml(haifa_kml)


@pytest.fixture
def utm_haifa_polygon(gcs_haifa_polygon: shapely.Polygon) -> shapely.Polygon:
    return gcs_polygon_to_utm_polygon(gcs_haifa_polygon)


@pytest.mark.parametrize("lon_lat", [
    (shapely.Point(34.962316, 32.835565),),
    (shapely.Point(35.000328, 32.825192),),
    (shapely.Point(34.910345, 32.842013),),
    (shapely.Point(34.9465170, 32.7470367),),
])
def test_haifa_gcs_coordinates_in_polygon(gcs_haifa_polygon: shapely.Polygon, lon_lat: shapely.Point):
    assert gcs_haifa_polygon.contains(lon_lat)


@pytest.mark.parametrize("xy", [
    (shapely.Point(683665.57, 3634763.72),),
    (shapely.Point(687245.73, 3633680.25),),
    (shapely.Point(678787.59, 3635389.50),),
    (shapely.Point(682367.29, 3624920.10),),
])
def test_haifa_utm_coordinates_in_polygon(utm_haifa_polygon: shapely.Polygon, xy: shapely.Point):
    assert utm_haifa_polygon.contains(xy)


@pytest.mark.parametrize("lon_lat", [
    (shapely.Point(34.991702, 32.828799),),
    (shapely.Point(34.655685, 32.899678),),
    (shapely.Point(34.946519, 32.747045),),
])
def test_haifa_gcs_coordinates_out_of_polygon(gcs_haifa_polygon: shapely.Polygon, lon_lat: shapely.Point):
    assert not gcs_haifa_polygon.contains(lon_lat)


@pytest.mark.parametrize("xy", [
    (shapely.Point(686430.60, 3634064.96),),
    (shapely.Point(654850.90, 3641380.81),),
    (shapely.Point(682367.46, 3624920.99),),
])
def test_haifa_utm_coordinates_out_of_polygon(utm_haifa_polygon: shapely.Polygon, xy: shapely.Point):
    assert not utm_haifa_polygon.contains(xy)


def test_point_on_the_edge(gcs_haifa_polygon: shapely.Polygon, utm_haifa_polygon: shapely.Polygon):
    gcs_point = shapely.Point(34.946521, 32.747061)
    utm_same_point = shapely.Point(682367.62, 3624922.76)
    assert gcs_haifa_polygon.contains(gcs_point)
    assert not utm_haifa_polygon.contains(utm_same_point)
