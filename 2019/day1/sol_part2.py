def main():
    with open("mass_p2.txt") as f:
        data = f.read()
        all_sums = []
        for mass in data.split():
            temp_sum = 0
            result = int(mass)
            while True:
                result = (int(result / 3)-2)
                if result <= 0:
                    break
                else:
                    temp_sum += result
            all_sums.append(temp_sum)
        return sum(all_sums)


if __name__ == "__main__":
    print(main())
