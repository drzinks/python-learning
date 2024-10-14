import time

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

def get_execution_time(message,func,n):
    start = time.perf_counter()
    func(n)
    return '{:f}'.format(round(time.perf_counter() - start, 8))

function_name_to_execution_time = {}

while(True):
    n = int(input("Put integer to which sum is done (from 1)"))
    function_name_to_execution_time["count_sum_to_n1"] = get_execution_time("count_sum_to_n1", count_sum_to_n1,n)
    function_name_to_execution_time["count_sum_to_n2"] = get_execution_time("count_sum_to_n2", count_sum_to_n2,n)
    function_name_to_execution_time["count_sum_to_n3"] = get_execution_time("count_sum_to_n3", count_sum_to_n3,n)
    function_name_to_execution_time["count_sum_to_n4"] = get_execution_time("count_sum_to_n4", count_sum_to_n4,n)
    function_name_to_execution_time["count_sum_to_n5"] = get_execution_time("count_sum_to_n5", count_sum_to_n5,n)
    sorted_values = sorted( ((v,k) for k,v in function_name_to_execution_time.items()))
    for value in sorted_values:
        print(value, "\n")

