from pathlib import Path

from py_static_dtm.static_dtm import CoordinateSystem, StaticDTM


def test_staticdtm_haifa_utm_coordinates_in_polygon(haifa_kml_file_path: Path):
    haifa_static_dtm = StaticDTM.from_kml_file(haifa_kml_file_path,
                                               CoordinateSystem.GCS,
                                               static_z=1)
    assert haifa_static_dtm.get_z_for_utm_coordinate(683665.57,
                                                     3634763.72) == 1
