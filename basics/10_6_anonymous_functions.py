def double(x):
    return x*2

print(double(2))
my_list = [2,14,22,7,6,4,5,17]
print(my_list)
my_list_filtered = list(filter(lambda e: e%2 == 0, my_list))
print(my_list_filtered)
my_list_filtered2 = [e for e in my_list if(e%2==0)]
print(my_list_filtered2)

