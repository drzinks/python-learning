def hello(name):
    print("Hello ", name ,". Welcome to my program")

hello("Michał")
hello("Wiolu")

def rectangular_surface(a,b):
    return a*b

print(rectangular_surface(3,4))

list1 = list(range(-5,6))

def sum_all_positve_numbers(list):
    return sum(
        number for number in list
        if(number>0)
        )

print(sum_all_positve_numbers(list1))


