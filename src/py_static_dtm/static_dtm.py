from dataclasses import dataclass
from pathlib import Path

import numpy as np
import shapely  # type: ignore
from fastkml import kml  # type: ignore

from py_static_dtm.kml_utils import polygon_from_kml
from py_static_dtm.polygon_utils import (CoordinateSystem,
                                         convert_polygon_to_utm)


@dataclass
class StaticDTM:
    utm_polygon: shapely.Polygon
    static_z: float

    @classmethod
    def from_kml_file(cls, kml_path: Path, coordinate_system: CoordinateSystem,
                      static_z: float):
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
