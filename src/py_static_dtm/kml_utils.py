import shapely  # type: ignore
from fastkml import geometry, kml  # type: ignore


def get_document_from_kml(kml_obj: kml.KML) -> kml.Document:
    all_documents_in_file = list(kml_obj.features())
    assert len(all_documents_in_file
               ) == 1, "Found more then one document in the file."
    document = all_documents_in_file[0]
    assert isinstance(
        document,
        kml.Document), "The document in the file is not a valid document"
    return document


def get_polygon_from_kml_document(document: kml.Document) -> geometry.Polygon:
    all_haifa_placemarks = list(document.features())
    assert len(
        all_haifa_placemarks
    ) == 1, "Found more then one placemark (polygon / line / point) " \
        "in the file."
    haifa_placemark = all_haifa_placemarks[0]
    assert isinstance(
        haifa_placemark,
        kml.Placemark), "The placemark in the file is not a valid placemark"
    polygon = haifa_placemark.geometry
    assert isinstance(
        polygon,
        geometry.Polygon), "The placemark in the file is not a polygon"
    return polygon


def polygon_from_kml(kml_obj: kml.KML) -> shapely.Polygon:
    document = get_document_from_kml(kml_obj)
    gcs_polygon = get_polygon_from_kml_document(document)
    return shapely.Polygon(shell=gcs_polygon.exterior.coords)
