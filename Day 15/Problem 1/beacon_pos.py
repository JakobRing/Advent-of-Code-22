import numpy as np


if __name__ == "__main__":
    y = 2000000
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

    blocked_for_beacon_count = 0
    for x in range(x_min, x_max+1):     # curr_pos = (x, y)
        if (x,y) in beacons:
            continue
        for s in sensor_data:
            if abs(s[0][0]-x)+abs(s[0][1]-y) <= s[1]:
                blocked_for_beacon_count += 1
                break
    print(f"{blocked_for_beacon_count} places are blocked in row {y} for beacons")
