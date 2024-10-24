def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        print("before yield: ",number)
        number = yield number * number #here the send method sets number
        print("aftery yield: ",number)

number_generator = number_multiplied_by_itself_generator()
#next(number_generator) #initiate generator
number_generator.send(None)

print("for debug purpose")