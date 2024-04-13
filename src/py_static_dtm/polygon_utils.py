import enum
from typing import Tuple

import shapely  # type: ignore
from pyproj import Proj  # type: ignore


class CoordinateSystem(enum.Enum):
    GCS = enum.auto
    UTM = enum.auto


def gcs_to_utm(
        lon_lat_alt: Tuple[float, float, float]) -> Tuple[float, float, float]:
    ISRAEL_ZONE = 36
    longitude, latitude, altitude = lon_lat_alt
    _proj = Proj(proj="utm", zone=ISRAEL_ZONE, ellps="WGS84")
    x, y = _proj(longitude, latitude)
    return x, y, altitude


def gcs_polygon_to_utm_polygon(
        gcs_polygon: shapely.Polygon) -> shapely.Polygon:
    utm_coordinates = tuple(gcs_to_utm(c) for c in gcs_polygon.exterior.coords)
    utm_polygon = shapely.Polygon(utm_coordinates)
    return utm_polygon


def convert_polygon_to_utm(
        polygon: shapely.Polygon,
        coordinate_system: CoordinateSystem) -> shapely.Polygon:
    if coordinate_system == CoordinateSystem.GCS:
        return gcs_polygon_to_utm_polygon(polygon)
    elif coordinate_system == CoordinateSystem.UTM:
        return polygon
    else:
        raise NotImplementedError(
            f"Polygons using {coordinate_system} coordinate system "
            "is not supported yet.")
