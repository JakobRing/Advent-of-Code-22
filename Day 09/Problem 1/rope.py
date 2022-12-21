
import numpy as np


def do_move(curr_move: str, head: [int], tail: [int]):
    if curr_move == "U":
        head[1] += 1
    elif curr_move == "D":
        head[1] -= 1
    elif curr_move == "R":
        head[0] += 1
    elif curr_move == "L":
        head[0] -= 1
    else:
        raise Exception("move not supported")
    if head[0] == tail[0] and abs(head[1] - tail[1]) == 2:      # same column
        tail[1] += np.sign(head[1] - tail[1])
    elif head[1] == tail[1] and abs(head[0] - tail[0]) == 2:      # same row
        tail[0] += np.sign(head[0] - tail[0])
    elif head[0] != tail[0] and head[1] != tail[1]:
        diff_width = head[0] - tail[0]      # > 0 => head above tail
        diff_height = head[1] - tail[1]     # > 0 => head right of tail
        if abs(diff_width) >= 2 or abs(diff_height) >= 2:
            tail[0] += np.sign(diff_width)
            tail[1] += np.sign(diff_height)
    return head, tail


if __name__ == "__main__":
    h = [0, 0]
    t = [0, 0]
    t_visited = [t.copy()]
    f = open("moves.txt")
    for line in f:
        move, count = line.strip().strip("\n").split(" ")
        for _ in range(int(count)):
            #print(f"h: {h}, t: {t}")
            h, t = do_move(move, h, t)
            t_visited.append(t.copy())
    print(t_visited)
    print(len(set(tuple(element) for element in t_visited)))
