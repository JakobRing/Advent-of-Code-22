
if __name__ == "__main__":
    priority_sum = 0
    f = open("rucksacks.txt")
    nextline = next(f)
    while nextline:
        rucksack1 = set(nextline[:-1])
        rucksack2 = set(next(f)[:-1])
        rucksack3 = set(next(f)[:-1])
        group = rucksack1.intersection(rucksack2).intersection(rucksack3)
        ascii_value = ord(group.pop())
        if 65 <= ascii_value <= 90:      # big letter
            priority_sum += ascii_value - 38
        elif 97 <= ascii_value <= 122:    # small letter
            priority_sum += ascii_value - 96
        else:
            raise Exception("No letter in the Input")
        try:
            nextline = next(f)
        except StopIteration:
            break
    print(f"The sum of the priorities is {priority_sum}")
