def generator():
    x = 0
    while True:
        x = x + 1
        print(f"1. Przed yield, x = {x}")
        x = yield x * x
        print(f"2. Po yield, x = {x}")

g = generator()
numbers = []
for _ in range(1,10):
    numbers.extend(next(g))
print(numbers)
wynik = g.send(15)
wynik2 = next(g)
print(wynik)