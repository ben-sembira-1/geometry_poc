from shapely import Polygon, Point  # type: ignore


def main():
    vertices = ((0, 0), (1, 0), (1, 1), (0, 1))
    my_polygon = Polygon(shell=vertices)
    my_point = Point(0, 0.9)
    print(f"{my_polygon=}, {my_point=}")
    print(f"{my_polygon.contains(my_point)=}")


if __name__ == "__main__":
    main()
