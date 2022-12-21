
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
    find_signal_strengths = [20, 60, 100, 140, 180, 220]
    sum_signal_strengths = 0
    for e in find_signal_strengths:
        sum_signal_strengths += cycle_values[e-1] * e
    print(f"Sum of the signal strengths: {sum_signal_strengths}")
