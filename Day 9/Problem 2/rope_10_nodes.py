
import numpy as np


def do_single_knot_move(head: [int], tail: [int]):
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
    return tail


def do_move(curr_move: str, this_rope: [[int]]):
    if curr_move == "U":
        this_rope[0][1] += 1
    elif curr_move == "D":
        this_rope[0][1] -= 1
    elif curr_move == "R":
        this_rope[0][0] += 1
    elif curr_move == "L":
        this_rope[0][0] -= 1
    else:
        raise Exception("move not supported")
    for i in range(1, 10):
        this_rope[i] = do_single_knot_move(this_rope[i-1], this_rope[i])
    return this_rope


if __name__ == "__main__":
    rope = [[0, 0] for _ in range(10)]
    t_visited = [rope[-1].copy()]
    f = open("moves.txt")
    for line in f:
        move, count = line.strip().strip("\n").split(" ")
        for _ in range(int(count)):
            rope = do_move(move, rope)
            t_visited.append(rope[-1].copy())
    #print(t_visited)
    print(len(set(tuple(element) for element in t_visited)))
