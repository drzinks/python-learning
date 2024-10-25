def generator():
    x = 1
    while True:
        sent_value = yield x * x  # Tutaj x może stać się None
        x = sent_value if sent_value is not None else x + 1  # Używamy wartości z send() lub zwiększamy x

g = generator()

numbers = []
for _ in range(1, 10):
    numbers.append(next(g))
print(numbers)

wynik = g.send(15)
wynik2 = next(g)
wynik3 = g.send(5)
print(wynik)
print(wynik2)
print(wynik3)