# line: tuple[tuple[int, int], tuple[int, int]]
# line (x1, y1), (x2, y2)
def intersection(line1: tuple[tuple[float, float], tuple[float, float]],
                  line2: tuple[tuple[float, float], tuple[float, float]]
                  ) -> tuple[float]:
    k1 = (line1[1][1] - line1[0][1])/(line1[1][0] - line1[0][0])
    k2 = (line2[1][1] - line2[0][1])/(line2[1][0] - line2[0][0])
    # если паралельны
    if k1 == k2:
        return False
    intersection_x = round(((line2[0][1] - k2 * line2[0][0]) -
                      (line1[0][1] - k1 * line1[0][0])) / (k1 - k2), 3)
    intersection_y = round(k1 * intersection_x + (line1[0][1] - k1 * line1[0][0]), 3)
    # если x y пренадлежат этим двум отрезкам
    if all([min(line[0][0], line[1][0]) <= intersection_x <= max(
            line[0][0], line[1][0]) and
            min(line[0][1], line[1][1]) <= intersection_y <= max(
            line[0][1], line[1][1])
            for line in (line1, line2)]):
        return intersection_x, intersection_y
    else:
        return False


if __name__ == "__main__":
    ab = (-2, 1), (3, 5)
    cd = (1, 4), (6, 2)
    print(intersection(*ab[0], *ab[1], *cd[0], *cd[1]))
