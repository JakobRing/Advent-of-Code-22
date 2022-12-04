
if __name__ == "__main__":
    contain = 0
    f = open("../sections.txt")
    for line in f:
        fst_section, snd_section = [section.split("-") for section in line.strip().strip("\n").split(",")]
        if int(snd_section[0]) <= int(fst_section[0]) <= int(snd_section[1]) \
           and int(snd_section[0]) <= int(fst_section[1]) <= int(snd_section[1]):           # first section in second
            contain += 1
        elif int(fst_section[0]) <= int(snd_section[0]) <= int(fst_section[1]) \
                and int(fst_section[0]) <= int(snd_section[1]) <= int(fst_section[1]):      # second section in first
            contain += 1
    f.close()
    print(f"Number of overlaps: {contain}")
