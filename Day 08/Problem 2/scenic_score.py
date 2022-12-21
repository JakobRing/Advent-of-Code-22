
import numpy as np

if __name__ == "__main__":
    f = open("trees.txt")
    tree_map = np.array([list(map(int, list(line.strip().strip("\n")))) for line in f])
    visible_count = 2 * ((tree_map.shape[0]-1) + (tree_map.shape[0]-1))     # trees on the edges
    for i_row in range(1, tree_map.shape[0]-1):
        for j_column in range(1, tree_map.shape[1]-1):
            if np.amax(tree_map[i_row, :j_column]) < tree_map[i_row, j_column] \
                    or np.amax(tree_map[i_row, (j_column+1):]) < tree_map[i_row, j_column] \
                    or np.amax(tree_map[:i_row, j_column]) < tree_map[i_row, j_column] \
                    or np.amax(tree_map[(i_row+1):, j_column]) < tree_map[i_row, j_column]:
                visible_count += 1
    print(visible_count)
