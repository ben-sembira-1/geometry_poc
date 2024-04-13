from dataclasses import dataclass
import enum
from pathlib import Path
from fastkml import kml  # type: ignore
import numpy as np
import shapely  # type: ignore

from fastkml_poc import gcs_polygon_to_utm_polygon, polygon_from_kml


class CoordinateSystem(enum.Enum):
    GCS = enum.auto
    UTM = enum.auto


def convert_polygon_to_utm(polygon: shapely.Polygon, coordinate_system: CoordinateSystem) -> shapely.Polygon:
    if coordinate_system == CoordinateSystem.GCS:
        return gcs_polygon_to_utm_polygon(polygon)
    elif coordinate_system == CoordinateSystem.UTM:
        return polygon
    else:
        raise NotImplementedError(
            f"Polygons using {coordinate_system} coordinate system is not supported yet.")


@dataclass
class StaticDTM:
    utm_polygon: shapely.Polygon
    static_z: float

    @classmethod
    def from_kml_file(cls, kml_path: Path, coordinate_system: CoordinateSystem, static_z: float):
        kml_obj = kml.KML()
        kml_obj.from_string(kml_path.read_bytes())
        polygon = polygon_from_kml(kml_obj)
        utm_polygon = convert_polygon_to_utm(polygon, coordinate_system)
        return cls(utm_polygon, static_z)

    def get_z_for_utm_coordinate(self, x: float, y: float) -> float:
        if self.utm_polygon.contains(shapely.Point(x, y)):
            return self.static_z
        else:
            return np.nan