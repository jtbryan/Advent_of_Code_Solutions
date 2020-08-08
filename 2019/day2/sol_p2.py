def main(noun, verb):
    with open("opcode_input_p2.txt") as f:
        data = f.read()
        items = data.split(",")
        for i in range(0, len(items)):
            items[i] = int(items[i])
        items[1] = noun
        items[2] = verb
        pos = 0
        while pos < len(items):
            if items[pos] == 99:
                break
            elif items[pos] == 1:
                items[items[pos+3]] = items[items[pos+1]] + items[items[pos+2]]
            elif items[pos] == 2:
                items[items[pos+3]] = items[items[pos+1]] * items[items[pos+2]]
            pos = pos + 4
        return items[0]
if __name__ == "__main__":
    goal_num = 19690720
    for i in range(100):
        for j in range(100):
            if main(i, j) == goal_num:
                print(100 * i + j)
                break
