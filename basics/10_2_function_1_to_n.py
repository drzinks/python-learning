def print_numbers_n2(n):
    for numbers in range(1,n+1):
        print(numbers)
        
def count_sum_to_n1(n):
    sum = 0;
    for number in range(1,n+1):
        sum += number
    return sum

def count_sum_to_n2(n):
    return sum([number for number in range(1,n+1)]) #list

def count_sum_to_n3(n):
    return sum({number for number in range(1,n+1)}) #set

def count_sum_to_n4(n):
    return sum(number for number in range(1,n+1)) #generator

def count_sum_to_n5(n):
    return int(((1+n)/2)*n)

print_numbers_n2(5)

while(True):
    number = int(input("Podaj liczbe całkowitą do której mam zliczyć sumę:"))
    if(number == 0):
        break
    print(count_sum_to_n1(number),"\n")
    print(count_sum_to_n2(number),"\n")
    print(count_sum_to_n3(number),"\n")
    print(count_sum_to_n4(number),"\n")
    print(count_sum_to_n5(number),"\n")
