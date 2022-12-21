
if __name__ == "__main__":
    f = open("marker_input.txt")
    line = next(f).strip().strip("\n").strip("\r")
    i = 4
    marker_test = line[i-4:i]
    while len(set(marker_test)) != 4:
        i += 1
        marker_test = line[i-4:i]
    print(f"A marker was found after {i} characters")
