import os
import sys
from datetime import datetime


def calculate(x, y):
    if x > y:
        print("x is bigger")
    else:
        print("y is bigger")
    return x + y


class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello,{self.name} you are {self.age}years old")


def main():
    result = calculate(10, 5)
    u = user("Ariel", 25)
    u.greet()
    print("Result is:", result)


if __name__ == "__main__":
    main()
