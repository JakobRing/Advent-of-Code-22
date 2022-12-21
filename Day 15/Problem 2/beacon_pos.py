import numpy as np
import sympy as sp


if __name__ == "__main__":
    x_max = y_max = -np.inf
    x_min = y_min = np.inf
    sensor_data = []    # list of [[x, y], absolute distance to the nearest beacon]
    beacons = set()        # list of (x,y)
    f = open("sensor.txt")
    while True:
        line = next(f, None)
        if not line:
            break
        # Sensor at x=3842919, y=126080: closest beacon is at x=3943893, y=1918172
        elements = line.strip(" \n").split(" ")
        x_sensor = int(elements[2][2:-1])
        y_sensor = int(elements[3][2:-1])
        x_beacon = int(elements[8][2:-1])
        y_beacon = int(elements[9][2:])
        beacons.add((x_beacon, y_beacon))

        x_min = min([x_sensor - abs(x_beacon-x_sensor), x_beacon - abs(x_beacon-x_sensor), x_min])
        x_max = max([x_sensor + abs(x_beacon-x_sensor), x_beacon + abs(x_beacon-x_sensor), x_max])
        y_min = min([y_sensor - abs(y_beacon-y_sensor), y_beacon - abs(y_beacon-y_sensor), y_min])
        y_max = max([y_sensor + abs(y_beacon-y_sensor), y_beacon + abs(y_beacon-y_sensor), y_max])
        sensor_data.append([[x_sensor, y_sensor], abs(x_beacon-x_sensor)+abs(y_beacon-y_sensor)])
    print(sensor_data)
    print(f"x_min: {x_min}, x_max: {x_max}, y_min: {y_min}, y_max: {y_max}")

    tuning_frequency_cords = []

    xy_min = 0
    xy_max = 4000000
    for y in range(xy_max, xy_min-1, -1):
        """intervals = sp.EmptySet  # intervals.empty()
        for s in sensor_data:
            r = abs(s[1] - abs(s[0][1] - y))
            left = s[0][0] - r
            right = s[0][0] + r
            intervals = sp.Union(intervals, sp.Interval(left, right))
        intersection = intervals.intersect(sp.Interval(xy_min, xy_max))
        if intersection.measure != xy_max-xy_min:
            print(f"{intersection} places are blocked in row {y} for beacons")
        if y % 4000 == 0:
            print(y)"""
        curr_interval = []
        for s in sensor_data:
            r = s[1] - abs(s[0][1] - y)
            left = max(xy_min, s[0][0] - r)
            right = min(xy_max, s[0][0] + r)
            if left <= right:
                curr_interval.append([left, right])
        # print(curr_interval)
        curr_interval = sorted(curr_interval, key=lambda x: x[0])
        union_interval = [curr_interval[0]]
        if [xy_min, xy_max] in curr_interval:
            union_interval = [[xy_min, xy_max]]
        else:
            for i in range(1, len(curr_interval)):
                if curr_interval[i][0] - 1 <= union_interval[-1][1]:        # [a, b] and [c, d] with c <= b
                    union_interval[-1] = [union_interval[-1][0], max(union_interval[-1][1], curr_interval[i][1])]
                elif curr_interval[i][0] - 1 > union_interval[-1][1]:
                    union_interval.append(curr_interval[i])
        if union_interval != [[xy_min, xy_max]]:
            print(f"y: {y}: interval: {union_interval}")
            break
        if y % 100000 == 0:
            print(y)
    # x * 4000000 + y == tuning_frequency
    print(f"tuning-frequency: {((union_interval[1][0] + union_interval[0][1]) // 2) * xy_max + y}")
