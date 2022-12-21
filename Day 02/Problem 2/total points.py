
if __name__ == "__main__":
    score = 0
    enemy = ["A", "B", "C"]             # Rock, Paper, Scissors
    me = ["X", "Y", "Z"]                # Rock, Paper, Scissors
    f = open("Strategy guide.txt")
    for line in f:
        his, how = line[0], line[2]
        if how == "X":      # lose
            my = me[enemy.index(his)-1]
        elif how == "Y":    # draw
            my = me[enemy.index(his)]
        elif how == "Z":    # win
            my = me[enemy.index(his)-2]

        if me.index(my) == enemy.index(his):    # draw
            score += 3
        elif (me.index(my) - enemy.index(his)) % 3 == 1:  # win
            score += 6
                                                # defeat else
        score += me.index(my) + 1
    f.close()
    print(f"Total score: {score}")
