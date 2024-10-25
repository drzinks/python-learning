class User:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age



michal = User("Michał", 42)
print(str(michal))

