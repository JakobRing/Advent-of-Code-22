
if __name__ == "__main__":
    priority_sum = 0
    f = open("rucksacks.txt")
    for rucksacks in f:
        cmp1 = set(rucksacks[:-1][:int(len(rucksacks)/2)])
        cmp2 = set(rucksacks[:-1][int(len(rucksacks) / 2):])
        both = cmp1.intersection(cmp2)
        ascii_value = ord(both.pop())
        if 65 <= ascii_value <= 90:      # big letter
            priority_sum += ascii_value - 38
        elif 97 <= ascii_value <= 122:    # small letter
            priority_sum += ascii_value - 96
        else:
            raise Exception("No letter in the Input")
    f.close()
    print(f"The sum of the priorities is {priority_sum}")
