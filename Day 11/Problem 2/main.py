from Monkey import Monkey
import re

if __name__ == "__main__":
    f = open("monkey.txt")
    monkey_list = []
    i_monkey_refs = []
    div_list = []
    line = next(f, None)
    while line:
        first_line = re.search('Monkey .*:', line)  # match "Monkey i:"
        if not first_line:
            raise Exception("not a monkey def")
        line = next(f, None)                        # match "  Starting items: a, b, ..."
        if line:
            starting_items = list(map(int, line.strip().strip("\n").replace(",", "").split(" ")[2:]))
        else:
            raise Exception("problem in the monkey def")
        line = next(f, None)                        # match "  Operation: new = old "
        if line:
            line = line.strip("\n").strip()
            prefix = re.search('Operation: new = ', line).group(0)
            op = line.removeprefix(prefix).strip()
        else:
            raise Exception("problem in the monkey def")
        line = next(f, None)                        # match: "  Test: divisible by int"
        if line:
            div_test = int(line.strip("\n").strip("").split(" ")[-1])
            div_list.append(div_test)
        else:
            raise Exception("problem in the monkey def")
        line = next(f, None)                        # match: "  If true: throw to monkey i"
        if line:
            curr_monkey_ref = [int(line.strip("\n").strip().split(" ")[-1])]
        else:
            raise Exception("problem in the monkey def")
        line = next(f, None)  # match: "  If false: throw to monkey i"
        if line:
            curr_monkey_ref.append(int(line.strip("\n").strip().split(" ")[-1]))
            i_monkey_refs.append(curr_monkey_ref)
        else:
            raise Exception("problem in the monkey def")
        line = next(f, None)  # match: "\n"
        line = next(f, None)  # next monkey
        monkey_list.append(Monkey(starting_items, op, div_test))

    divisor = 1
    for e in div_list:
        divisor = divisor * e
    for i in range(len(monkey_list)):
        monkey_list[i].add_monkey_refs(monkey_list[i_monkey_refs[i][0]], monkey_list[i_monkey_refs[i][1]])
        monkey_list[i].add_divisor(divisor)
    for i in range(10000):
        for monkey in monkey_list:
            monkey.inspect()
        if i % 100 == 0:
            print(f"round: {i}")
    monkey_business = []
    for i in range(len(monkey_list)):
        monkey_business.append(monkey_list[i].get_nr_items_inspected())
        print(f"Monkey {i} inspected items {monkey_list[i].get_nr_items_inspected()}")
    monkey_business.sort()
    print(f"monkey business: {monkey_business[-1] * monkey_business[-2]}")
