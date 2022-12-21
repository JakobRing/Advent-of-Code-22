from functools import cmp_to_key
import copy


def packet_order(p1, p2):
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)
    while len(p1) > 0 and len(p2) > 0:
        f1, f2 = p1.pop(0), p2.pop(0)
        if isinstance(f1, int) and isinstance(f2, int):
            if f1 < f2:                                     # int <= int
                first_check = -1
            elif f1 == f2:                                  # int == int
                first_check = 0
            else:                                           # int > int
                first_check = 1
        elif isinstance(f1, list) and isinstance(f2, list):
            first_check = packet_order(f1, f2)
        elif isinstance(f1, list) and isinstance(f2, int):
            first_check = packet_order(f1, [f2])
        elif isinstance(f1, int) and isinstance(f2, list):
            first_check = packet_order([f1], f2)
        else:
            raise Exception("problem with the packet order")
        if first_check == 1 or first_check == -1:
            return first_check
        elif first_check != 0:
            raise Exception("problem with the packet order")

    if len(p1) == 0 and len(p2) == 0:   # [] == []
        return 0
    elif len(p1) == 0:                  # [] < list
        return -1
    if len(p2) == 0:                    # list > []
        return 1


if __name__ == "__main__":
    div_packet_1 = [[2]]
    div_packet_2 = [[6]]
    packet_list = [div_packet_1, div_packet_2]
    f = open("packets.txt")
    line = next(f, None)
    while line:
        line = line.strip("\n ")
        if line != "":
            packet = eval(line)
            packet_list.append(packet)
        line = next(f, None)

    print(packet_list)
    packet_list = sorted(packet_list, key=cmp_to_key(packet_order))
    print(packet_list)
    i1 = packet_list.index(div_packet_1) + 1
    i2 = packet_list.index(div_packet_2) + 1
    print(f"decoder key: {i1*i2}")
