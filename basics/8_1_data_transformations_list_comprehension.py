#lists formulas
numbers = [1,2,3,4,5]
numbers2 = [number**2 for number in numbers]
print(numbers2)
even_numbers = [number
    for number in numbers
    if(number % 2 == 0)
    ]
print(even_numbers)
#generating formulas
evenNumberGenerator = (number for number in numbers if number%2==0)
number_generator = (number for number in range(101))
print(sum(number_generator))
number_generator = (number for number in range(101))
for number in number_generator:
    print(number)
print("###")

