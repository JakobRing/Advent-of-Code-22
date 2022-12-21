
if __name__ == "__main__":
    overlap = 0
    f = open("../sections.txt")
    for line in f:
        fst_section, snd_section = [section.split("-") for section in line.strip().strip("\n").split(",")]
        if int(fst_section[1]) < int(snd_section[0]) or int(snd_section[1]) < int(fst_section[0]):
            # second section is "over" the first section or first section is "over" the second section
            continue
        overlap += 1
    f.close()
    print(f"Number of overlaps: {overlap}")
