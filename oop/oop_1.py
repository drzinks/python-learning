class User:
    id = 0
    age = 0

    def __init__(self, name, age):
        User.id += 1
        self.name = name #zmienna klasowa
        self.age = age



michal = User("Michał", 42)
print(User.name)

