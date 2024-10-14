def greet_n_times(name, n=1):
    for i in range(0,n):
        print("Hello ",name)

def count(*args):
    return sum(arg for arg in args)

greet_n_times(n=5, name="Łukasz")


print(count(2,4,1,2,4,5,10))
