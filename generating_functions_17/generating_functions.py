

even_numbers_generator = (
    element
    for element in range(401)
    if (element %2 == 0)
)

def generate_even_numbers(how_many):
    for element in range(how_many +1):
        if (element %2 == 0) :
            print("before yield")
            yield element
    print("after yield")

def generate_10_numbers():
    x = 1
    while x<11:
        yield x
        x += 1

def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        print("returned number: ",number)
        yield number * number

even = generate_even_numbers(100)
print(next(even))
print(next(even))
print(next(even))
print(next(even))
ten_numbers_gen = generate_10_numbers()
print(list(ten_numbers_gen))


number_generator = number_multiplied_by_itself_generator()
generated_numbers = list()

for _ in range(10):
    generated_numbers.append(next(number_generator))

print(next(number_generator))
print("for debug purpose print")
# print(generated_numbers)
# print(next(number_generator))
# for _ in range(30):
#     generated_numbers.append(next(number_generator))
# print(generated_numbers)
