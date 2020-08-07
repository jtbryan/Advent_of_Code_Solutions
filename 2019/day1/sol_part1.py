def main():
    with open("mass.txt") as f:
        data = f.read()
        return sum((int(int(mass)/3)-2) for mass in data.split())



if __name__ == "__main__":
    print(main())
