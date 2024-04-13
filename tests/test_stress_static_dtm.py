import math
import time
from pathlib import Path

import numpy as np
import pytest
import shapely  # type: ignore
from haifa_points import (INSIDE_POLYGON_UTM, OUTSIDE_POLYGON_UTM,
                          SAME_ON_EDGE_OUTSIDE_POLYGON_UTM)

from py_static_dtm.static_dtm import CoordinateSystem, StaticDTM

STATIC_Z = 1


@pytest.fixture
def haifa_static_dtm(haifa_kml_file_path: Path) -> StaticDTM:
    return StaticDTM.from_kml_file(haifa_kml_file_path,
                                   CoordinateSystem.GCS,
                                   static_z=STATIC_Z)


@pytest.mark.slow
def test_static_dtm_performance(haifa_static_dtm: StaticDTM):
    MAX_RUN_TIME_SEC = 20
    TOTAL_AMOUNT_OF_QUERIES = 300_000
    QUERIES_PER_AXIS = int(math.sqrt(TOTAL_AMOUNT_OF_QUERIES))
    count = 0
    start_time = time.time()
    for x in np.linspace(669793.20, 678204.38, num=QUERIES_PER_AXIS):
        for y in np.linspace(3638760.56, 3631597.14, num=QUERIES_PER_AXIS):
            assert haifa_static_dtm.get_z_for_utm_coordinate(x, y) == STATIC_Z
            count += 1
    end_time = time.time()
    total_time = end_time - start_time
    assert total_time < MAX_RUN_TIME_SEC


@pytest.mark.parametrize("xy", INSIDE_POLYGON_UTM)
def test_staticdtm_haifa_utm_coordinates_in_polygon(
        haifa_static_dtm: StaticDTM, xy: shapely.Point):
    assert haifa_static_dtm.get_z_for_utm_coordinate(xy.x, xy.y) == STATIC_Z


@pytest.mark.parametrize("xy", OUTSIDE_POLYGON_UTM)
def test_haifa_utm_coordinates_out_of_polygon(haifa_static_dtm: StaticDTM,
                                              xy: shapely.Point):
    assert np.isnan(haifa_static_dtm.get_z_for_utm_coordinate(xy.x, xy.y))


def test_point_on_the_edge(haifa_static_dtm: StaticDTM):
    utm_same_point = SAME_ON_EDGE_OUTSIDE_POLYGON_UTM
    assert np.isnan(
        haifa_static_dtm.get_z_for_utm_coordinate(utm_same_point.x,
                                                  utm_same_point.y))
