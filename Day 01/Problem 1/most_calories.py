
if __name__ == "__main__":
    max_calories = 0
    buffer = 0
    f = open("calories_list.txt")
    for line in f:
        if line == "\n":
            max_calories = max(buffer, max_calories)
            buffer = 0
        else:
            buffer += int(line[:-1])
    f.close()
    print(f"The biggest value of calories is: {max_calories}")