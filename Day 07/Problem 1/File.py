

class File:
    def __init__(self, name: str, size: int):
        self.size = int(size)
        self.name = name

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name
