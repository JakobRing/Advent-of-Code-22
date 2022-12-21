
def packet_order(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        f1, f2 = p1.pop(0), p2.pop(0)
        if isinstance(f1, int) and isinstance(f2, int):
            if f1 < f2:                                     # int <= int
                first_check = 1
            elif f1 == f2:                                  # int == int
                first_check = 0
            else:                                           # int > int
                first_check = -1
        elif isinstance(f1, list) and isinstance(f2, list):
            first_check = packet_order(f1, f2)
        elif isinstance(f1, list) and isinstance(f2, int):
            first_check = packet_order(f1, [f2])
        elif isinstance(f1, int) and isinstance(f2, list):
            first_check = packet_order([f1], f2)
        else:
            raise Exception("problem with the packet order")
        if first_check == 1:
            return 1
        elif first_check == -1:
            return -1
        elif first_check != 0:
            raise Exception("problem with the packet order")

    if len(p1) == 0 and len(p2) == 0:   # [] <= []
        return 0
    elif len(p1) == 0:                  # [] <= list
        return 1
    if len(p2) == 0:                    # list > []
        return -1


if __name__ == "__main__":
    index_sum = []
    index = 1
    f = open("packets.txt")
    line1 = next(f, None)
    line2 = next(f, None)
    while line1 and line2:
        packet1 = eval(line1.strip("\n "))
        packet2 = eval(line2.strip("\n "))
        order = packet_order(packet1, packet2)
        if order == 1 or order == 0:  # packet1 <= packet2
            index_sum.append(index)
        elif order != -1:
            raise Exception("problem with the packet order")
        index += 1
        between_line = next(f, None)
        if between_line:
            if between_line.strip(" \n") == "":
                line1 = next(f, None)
                line2 = next(f, None)
            else:
                raise Exception("packet file isn't formatted right")
        else:
            break
    print(f"Sum of indices of right formatted lines: {sum(index_sum)} with indices: {index_sum}")
