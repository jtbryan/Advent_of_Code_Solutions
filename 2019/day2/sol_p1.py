def main():
    with open("opcode_input.txt") as f:
        data = f.read()
        items = data.split(",")
        for i in range(0, len(items)):
            items[i] = int(items[i])
        items[1] = 12
        items[2] = 2
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
    print(main())
