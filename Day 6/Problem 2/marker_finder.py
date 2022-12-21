
if __name__ == "__main__":
    marker_count = 14
    f = open("marker_input.txt")
    line = next(f).strip().strip("\n").strip("\r")
    i = marker_count
    marker_test = line[i-marker_count:i]
    while len(set(marker_test)) != marker_count:
        i += 1
        marker_test = line[i-marker_count:i]
    print(f"A marker was found after {i} characters")
