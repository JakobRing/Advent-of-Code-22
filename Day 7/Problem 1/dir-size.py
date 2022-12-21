
from Dir import Dir
from File import File

if __name__ == "__main__":
    fp = open("dir.txt")
    command = None      # current command as string
    current_dir = None  # pointer to current dir
    root = None         # pointer to root
    for line in fp:
        line_items = line.strip().strip("\n").strip("\r").split(" ")
        if line_items[0] == "$":  # command
            command = line_items[1]
            if command == "cd":
                if line_items[2] == "/":
                    current_dir = root = Dir(line_items[2], None)
                elif line_items[2] == "..":
                    current_dir = current_dir.get_parent()
                elif current_dir.has_subdir(line_items[2]):
                    current_dir = current_dir.get_subdir(line_items[2])
            elif command == "ls":
                continue
            else:
                raise Exception("operation not supported")
        else:               # output
            if line_items[0] == "dir" and len(line_items) == 2:
                current_dir.add_subdir(Dir(line_items[1], current_dir))
            elif len(line_items) == 2:
                current_dir.add_file(File(line_items[1], line_items[0]))
            else:
                raise Exception("ls output is wrong")
    print(root.get_sum_at_most_100000())
