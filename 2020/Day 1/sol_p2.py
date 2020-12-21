def main():
    nums = list()
    with open("./opcode_input_p2.txt") as f:
        line = f.read().split("\n")
        nums = line
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for index, num in enumerate(nums, start=0):
        for i2 in range (index, len(nums)):
            for i3 in range (i2, len(nums)):
                if num + nums[i2] + nums[i3] == 2020:
                    print(num*nums[i2]*nums[i3])
                    return
if __name__ == "__main__":
    main()