def add(a, b):
    return a + b


def long_function_name(var_one, var_two, var_three, var_four):
    if var_one == True:
        print("Something happened")
    else:
        print("Something else happened")
        if var_two == True:
            print("nested condition")


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name)


data = {"users": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]}


for u in data["users"]:
    user = User(u["name"], u["age"])
    user.greet()
    print(add(1, 2))


if __name__ == "__main__":
    long_function_name(True, False, True, False)
