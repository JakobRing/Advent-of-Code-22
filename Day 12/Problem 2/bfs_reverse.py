import numpy as np


if __name__ == "__main__":
    f = open("elevation.txt")
    elevation = []
    queue = []
    for line in f:
        elevation.append(list(line.strip("\n").strip()))

    for i in range(len(elevation)):
        if "S" in elevation[i]:
            start = (i, elevation[i].index("S"))
            elevation[start[0]][start[1]] = "a"
        if "E" in elevation[i]:
            end = (i, elevation[i].index("E"))
            elevation[end[0]][end[1]] = "z"
    elevation = list(map(lambda x: (list(map(ord, x))), elevation))

    elevation = np.array(elevation)
    d = np.full(elevation.shape, -1)
    d[end] = 0
    queue.append(end)

    while queue:
        curr_y, curr_x = queue.pop(0)
        curr_d = d[curr_y, curr_x]
        # dijkstra
        if curr_y > 0 and d[curr_y-1, curr_x] == -1 and (elevation[curr_y-1, curr_x] - elevation[curr_y, curr_x]) >= -1:
            # has element above that isn't reached already
            d[curr_y - 1, curr_x] = curr_d + 1
            queue.append((curr_y-1, curr_x))
            if elevation[curr_y-1, curr_x] == 97:
                print(d[curr_y-1, curr_x])
                break
        if curr_y < elevation.shape[0]-1 and d[curr_y+1, curr_x] == -1 and (elevation[curr_y+1, curr_x] - elevation[curr_y, curr_x]) >= -1:
            # has element below that isn't reached already
            d[curr_y + 1, curr_x] = curr_d + 1
            queue.append((curr_y + 1, curr_x))
            if elevation[curr_y+1, curr_x] == 97:
                print(d[curr_y+1, curr_x])
                break
        if curr_x > 0 and d[curr_y, curr_x-1] == -1 and (elevation[curr_y, curr_x-1] - elevation[curr_y, curr_x]) >= -1:
            # has element above that isn't reached already
            d[curr_y, curr_x - 1] = curr_d + 1
            queue.append((curr_y, curr_x-1))
            if elevation[curr_y, curr_x-1] == 97:
                print(d[curr_y, curr_x-1])
                break
        if curr_x < elevation.shape[1]-1 and d[curr_y, curr_x+1] == -1 and (elevation[curr_y, curr_x+1] - elevation[curr_y, curr_x]) >= -1:
            # has element below that isn't reached already
            d[curr_y, curr_x + 1] = curr_d + 1
            queue.append((curr_y, curr_x+1))
            if elevation[curr_y, curr_x+1] == 97:
                print(d[curr_y, curr_x+1])
                break
    print(elevation)
    print(d[end[0]][end[1]])
