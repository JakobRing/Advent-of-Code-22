
import numpy as np

if __name__ == "__main__":
    f = open("trees.txt")
    tree_map = np.array([list(map(int, list(line.strip().strip("\n")))) for line in f])
    scenic_score = np.ones(tree_map.shape)
    for i_row in range(0, tree_map.shape[0]):
        for j_column in range(0, tree_map.shape[1]):
            up = right = left = down = 1
            this_tree = tree_map[i_row, j_column]
            if i_row == 0:
                trees_up, trees_down = [], tree_map[i_row + 1:, j_column]
            elif i_row == tree_map.shape[0]:
                trees_up, trees_down = np.flip(tree_map[:i_row, j_column]), []
            else:
                trees_up, trees_down = np.flip(tree_map[:i_row, j_column]), tree_map[i_row + 1:, j_column]
            if j_column == 0:
                trees_left, trees_right = [], tree_map[i_row, j_column + 1:]
            elif j_column == tree_map.shape[1]:
                trees_left, trees_right = np.flip(tree_map[i_row, :j_column]), []
            else:
                trees_left, trees_right = np.flip(tree_map[i_row, :j_column]), tree_map[i_row, j_column + 1:]
            for i in range(len(trees_up)-1):
                if trees_up[i] >= this_tree:
                    break
                up += 1
            for i in range(len(trees_down)-1):
                if trees_down[i] >= this_tree:
                    break
                down += 1
            for i in range(len(trees_left)-1):
                if trees_left[i] >= this_tree:
                    break
                left += 1
            for i in range(len(trees_right)-1):
                if trees_right[i] >= this_tree:
                    break
                right += 1
            scenic_score[i_row, j_column] = up * right * left * down
    print(scenic_score)
    print(np.amax(scenic_score))
