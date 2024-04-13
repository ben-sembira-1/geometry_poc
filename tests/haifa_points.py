from typing import List

import shapely  # type:ignore

INSIDE_POLYGON_GCS: List[shapely.Point] = [
    shapely.Point(34.962316, 32.835565),
    shapely.Point(34.996019, 32.826362),
    shapely.Point(34.910345, 32.842013),
    shapely.Point(34.9465170, 32.7470367),
]

INSIDE_POLYGON_UTM: List[shapely.Point] = [
    shapely.Point(683665.57, 3634763.72),
    shapely.Point(686839.86, 3633802.36),
    shapely.Point(678787.59, 3635389.50),
    shapely.Point(682367.29, 3624920.10),
]

OUTSIDE_POLYGON_GCS: List[shapely.Point] = [
    shapely.Point(34.991702, 32.828799),
    shapely.Point(34.655685, 32.899678),
    shapely.Point(34.946519, 32.747045),
    shapely.Point(34.998646, 32.826047),
]

OUTSIDE_POLYGON_UTM: List[shapely.Point] = [
    shapely.Point(686430.60, 3634064.96),
    shapely.Point(654850.90, 3641380.81),
    shapely.Point(682367.46, 3624920.99),
    shapely.Point(687086.46, 3633772.08),
]

ON_EDGE_INSIDE_POLYGON_GCS: shapely.Point = shapely.Point(34.946521, 32.747061)
SAME_ON_EDGE_OUTSIDE_POLYGON_UTM: shapely.Point = shapely.Point(
    682367.62, 3624922.76)
