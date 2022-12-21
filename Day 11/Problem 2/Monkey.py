

class Monkey:

    def __init__(self, starting_items: [int], op: str, div_test: int):
        self.items_inspected = 0
        self.items = starting_items
        self.op = op    # use eval()
        self.div_test = lambda x: x % div_test == 0
        self.monkey1 = None
        self.monkey2 = None

    def add_monkey_refs(self, monkey1, monkey2):
        self.monkey1 = monkey1
        self.monkey2 = monkey2

    def add_divisor(self, divisor: int):
        self.divisor = divisor

    def add_item(self, item: int):
        self.items.append(item)

    def get_nr_items_inspected(self):
        return self.items_inspected

    def inspect(self):
        while self.items:
            old = self.items.pop(0)
            curr_item = int(eval(self.op))   # something like "old +/*..."
            curr_item = curr_item % self.divisor
            if self.div_test(curr_item) and self.monkey1:
                self.monkey1.add_item(curr_item)
            elif self.monkey2:
                self.monkey2.add_item(curr_item)
            else:
                raise Exception("Monkeys not referenced")
            self.items_inspected += 1
