import numpy as np


if __name__ == "__main__":
    f = open("add.txt")
    current_cycle = 0
    cycle_values = [1]  # during first cycle (value at i => cycles_values[i-1])
    for line in f:
        values = line.strip("\n").split(" ")
        if line.strip("\n") == "noop":
            cycle_values.append(cycle_values[-1])   # after next cycle the value of x doesn't change
        elif values[0] == "addx" and len(values) == 2:
            cycle_values.append(cycle_values[-1])
            cycle_values.append(cycle_values[-1] + int(values[1]))
        else:
            raise Exception("command not defined")
    cycle_values = cycle_values[:-1]
    crt = ['.']*len(cycle_values)
    print(cycle_values)
    for i in range(len(cycle_values)):
        if abs(cycle_values[i] - (i % 40)) <= 1:
            crt[i] = '#'
    draw = np.array(crt).reshape((6, 40))
    print(draw)
    for i in range(draw.shape[0]):
        print(f"{''.join(draw[i])}")
