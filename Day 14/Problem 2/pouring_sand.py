import numpy as np


def print_grid(grid_list):
    for i in range(len(grid_list)):
        print(f"{''.join(grid_list[i])}")


if __name__ == "__main__":
    rocks = []
    spawn_point = (500, 0)

    black = u"\u25A0"
    white = '.'
    sand = "O"

    f = open("rock.txt")
    line = next(f, None)
    while line:     # read in lines
        str_rocks = line.strip("\n ").split(" -> ")
        rocks.append([(int(e.split(",")[0]), int(e.split(",")[1])) for e in str_rocks])
        line = next(f, None)

    ymax = max(map(max, [list(zip(*e))[1] for e in rocks])) + 2
    ymin = min(min(map(min, [list(zip(*e))[1] for e in rocks])), 0)

    rocks.append([(spawn_point[0]-ymax - 1, ymax), (spawn_point[0] + ymax + 1, ymax)])  # infinite floor

    xmax = max(map(max, [list(zip(*e))[0] for e in rocks]))
    xmin = min(map(min, [list(zip(*e))[0] for e in rocks]))

    rock_points = []        # get all points for the rocks
    for rock_line in rocks:
        for i in range(len(rock_line)-1):
            if rock_line[i][0] == rock_line[i+1][0]:    # same width
                for d in range(min(rock_line[i][1], rock_line[i+1][1]), max(rock_line[i][1], rock_line[i+1][1])+1):
                    rock_points.append((rock_line[i][0], d))
            if rock_line[i][1] == rock_line[i+1][1]:    # same height
                for d in range(min(rock_line[i][0], rock_line[i+1][0]), max(rock_line[i][0], rock_line[i+1][0])+1):
                    rock_points.append((d, rock_line[i][1]))

    grid = np.full(((ymax - ymin + 1), (xmax - xmin + 1)), white)   # fill 2d grid
    grid[spawn_point[1]-ymin][spawn_point[0]-xmin] = '+'
    for points in rock_points:
        grid[points[1] - ymin][points[0] - xmin] = black
    print_grid(grid)
    print(f"xmin: {xmin}, xmax: {xmax}, ymin: {ymin}, ymax: {ymax}")
    sand_count = 0
    while grid[spawn_point[1]-ymin][spawn_point[0]-xmin] != sand:
        curr_point = [spawn_point[0], spawn_point[1]]
        while True:
            if grid[curr_point[1]-ymin+1][curr_point[0]-xmin] not in [black, sand]:     # under the current point is free space
                curr_point[1] += 1
            elif grid[curr_point[1]-ymin+1][curr_point[0]-xmin-1] not in [black, sand]: # left under the current point is free space
                curr_point[1] += 1
                curr_point[0] -= 1
            elif grid[curr_point[1]-ymin+1][curr_point[0]-xmin+1] not in [black, sand]: # right under the current point is free space
                curr_point[1] += 1
                curr_point[0] += 1
            else:                                                                       # sand rests at the place
                grid[curr_point[1] - ymin][curr_point[0] - xmin] = sand
                sand_count += 1
                break
    print_grid(grid)
    print(f"sand count: {sand_count}")
