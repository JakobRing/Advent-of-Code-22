
from File import File


class Dir:
    def __init__(self, name: str, parent):
        self.name = name
        self.subdirs = []
        self.subfiles = []
        self.parent = parent

    def add_file(self, f: File):
        self.subfiles.append(f)

    def add_subdir(self, d):
        self.subdirs.append(d)

    def get_size(self) -> int:
        sum = 0
        for d in self.subdirs:
            sum += d.get_size()
        for f in self.subfiles:
            sum += f.get_size()
        return sum

    def get_name(self):
        return self.name

    def has_subdir(self, name: str) -> bool:
        for d in self.subdirs:
            if d.get_name() == name:
                return True
        return False

    def get_subdir(self, name: str):
        for d in self.subdirs:
            if d.get_name() == name:
                return d
        return None

    def get_parent(self):
        return self.parent

    def get_sum_at_most_100000(self) -> int:
        selfsize = self.get_size()
        if selfsize <= 100000:
            sum = selfsize
        else:
            sum = 0
        for d in self.subdirs:
            sum += d.get_sum_at_most_100000()
        return sum
