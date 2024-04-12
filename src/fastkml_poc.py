from typing import Tuple
from fastkml import kml, geometry  # type: ignore
from pathlib import Path
from pyproj import Proj  # type: ignore
import shapely  # type: ignore


def get_document_from_kml(kml_obj: kml.KML) -> kml.Document:
    all_documents_in_file = list(kml_obj.features())
    assert len(
        all_documents_in_file) == 1, "Found more then one document in the file."
    document = all_documents_in_file[0]
    assert isinstance(
        document, kml.Document), "The document in the file is not a valid document"
    return document


def get_polygon_from_kml_document(document: kml.Document) -> geometry.Polygon:
    all_haifa_placemarks = list(document.features())
    assert len(
        all_haifa_placemarks) == 1, "Found more then one placemark (polygon / line / point) in the file."
    haifa_placemark = all_haifa_placemarks[0]
    assert isinstance(
        haifa_placemark, kml.Placemark), "The placemark in the file is not a valid placemark"
    polygon = haifa_placemark.geometry
    assert isinstance(
        polygon, geometry.Polygon), "The placemark in the file is not a polygon"
    return polygon


class LonLatAlt:
    __slots__ = ("longitude", "latitude", "altitude")

    def __init__(self, lon_lat_alt: Tuple[float, float, float]):
        self.longitude = lon_lat_alt[0]
        self.latitude = lon_lat_alt[1]
        self.altitude = lon_lat_alt[2]

    def to_utm_tuple(self) -> Tuple[float, float, float]:
        ISRAEL_ZONE = 36
        _proj = Proj(proj='utm', zone=ISRAEL_ZONE, ellps='WGS84')
        x, y = _proj(self.longitude, self.latitude)
        return x, y, self.altitude


def gcs_polygon_from_kml(kml_obj: kml.KML) -> shapely.Polygon:
    document = get_document_from_kml(kml_obj)
    gcs_polygon = get_polygon_from_kml_document(document)
    return shapely.Polygon(shell=gcs_polygon.exterior.coords)


def gcs_polygon_to_utm_polygon(gcs_polygon: shapely.Polygon) -> shapely.Polygon:
    utm_coordinates = tuple(LonLatAlt(c).to_utm_tuple()
                            for c in gcs_polygon.exterior.coords)
    utm_polygon = shapely.Polygon(utm_coordinates)
    return utm_polygon


def main():
    haifa_kml = kml.KML()
    haifa_kml.from_string(Path("./HaifaSea.kml").read_bytes())
    gcs_polygon = gcs_polygon_from_kml(haifa_kml)
    utm_polygon = gcs_polygon_to_utm_polygon(gcs_polygon)
    print(gcs_polygon.contains(shapely.Point(34.962316, 32.835565)))
    print(utm_polygon.contains(shapely.Point(683665.57, 3634763.72)))


if __name__ == "__main__":
    main()
