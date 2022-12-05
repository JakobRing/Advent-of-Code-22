
if __name__ == "__main__":
    f = open("../crates.txt")
    stacks_pre = [next(f)]
    while stacks_pre[-1].strip().strip("\n") != "":       # get stacks at the beginning
        stacks_pre.append(next(f))

    stacks_pre.pop(-1)                                                  # blank line
    numbers = int(stacks_pre.pop(-1).strip().strip("\n").split(" ")[-1])     # number line
    crate_stacks = ["" for i in range(numbers)]

    for line in stacks_pre:
        for i in range(0, int(len(line)/4)):   # i = 0, 1, 2 =>  to chars at 1, 5, 9, ...
            if line[4*i+1] != " ":
                crate_stacks[i] = line[4*i+1] + crate_stacks[i]     # last element of string in on top of the stack

    line = next(f, None)
    while line:             # line = "move {count} from {starting_point} to {destination+1}"
        command = line.strip().strip("\n").split(" ")
        if command[0] != 'move' or command[2] != 'from' or command[4] != 'to':
            raise Exception("Not the wanted command_line")
        else:   # count last elements of string to the end of the destination string + remove at starting_point
            crate_stacks[int(command[5])-1] += crate_stacks[int(command[3])-1][-int(command[1]):]
            crate_stacks[int(command[3])-1] = crate_stacks[int(command[3])-1][:-int(command[1])]
        line = next(f, None)
    print(crate_stacks)
    print("".join([stack[-1] for stack in crate_stacks]))
    f.close()
