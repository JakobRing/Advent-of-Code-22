
if __name__ == "__main__":
    list = []
    buffer = 0
    f = open("calories_list.txt")
    for line in f:
        if line == "\n":
            list.append(buffer)
            buffer = 0
        else:
            buffer += int(line[:-1])
    f.close()
    list.sort(reverse=True)
    print(f"The biggest 3 values of calories are: {sum(list[:3])}")