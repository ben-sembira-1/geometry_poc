import math
import time
import pytest
from pathlib import Path

import numpy as np
from static_dtm.static_dtm import StaticDTM, CoordinateSystem


STATIC_Z = 1


@pytest.fixture
def haifa_static_dtm(haifa_kml_file_path: Path) -> StaticDTM:
    return StaticDTM.from_kml_file(haifa_kml_file_path, CoordinateSystem.GCS, static_z=STATIC_Z)


def test_static_dtm_single_values(haifa_static_dtm: StaticDTM):
    assert haifa_static_dtm.get_z_for_utm_coordinate(
        683665.57, 3634763.72) == STATIC_Z
    assert np.isnan(haifa_static_dtm.get_z_for_utm_coordinate(
        686430.60, 3634064.96))


@pytest.mark.slow
def test_static_dtm_performance(haifa_static_dtm: StaticDTM):
    MAX_RUN_TIME_SEC = 10
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
