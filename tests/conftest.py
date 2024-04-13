from pathlib import Path

import pytest
import shapely  # type: ignore
from fastkml import kml  # type: ignore

from py_static_dtm.kml_utils import polygon_from_kml
from py_static_dtm.polygon_utils import gcs_polygon_to_utm_polygon


@pytest.fixture
def haifa_kml_file_path() -> Path:
    return Path(__file__).parent / "HaifaSea.kml"


@pytest.fixture
def haifa_kml(haifa_kml_file_path: Path) -> kml.KML:
    haifa_kml = kml.KML()
    haifa_kml.from_string(haifa_kml_file_path.read_bytes())
    return haifa_kml


@pytest.fixture
def gcs_haifa_polygon(haifa_kml: kml.KML) -> shapely.Polygon:
    return polygon_from_kml(haifa_kml)


@pytest.fixture
def utm_haifa_polygon(gcs_haifa_polygon: shapely.Polygon) -> shapely.Polygon:
    return gcs_polygon_to_utm_polygon(gcs_haifa_polygon)
