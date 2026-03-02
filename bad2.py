def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    if a > b:
        print("a bigger")
    else:
        print("b bigger")
    return a - b


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name:", self.name, " Age:", self.age)


def main():
    result = add_numbers(5, 3)
    res2 = subtract_numbers(10, 20)
    p = person("Bob", 30)
    p.info()
    print("Results:", result, res2)


if __name__ == "__main__":
    main()
