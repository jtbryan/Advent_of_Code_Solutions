def main():
    nums = list()
    with open("./opcode_input.txt") as f:
        line = f.read().split("\n")
        nums = line
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for index, num in enumerate(nums, start=0):
        for i2 in range (index, len(nums)):
            if num + nums[i2] == 2020:
                print(num*nums[i2])
                return
if __name__ == "__main__":
    main()