namesToAge = {
    "Michał" : 42,
    "Maciej" : 43,
    "Jaroslaw" : 35,
    "Sprawny" : 40,
    }

namesToLength = { #czytac od for do prawej i dopiero poczatek
        name : len(name)
        for name in namesToAge
        if name.startswith("M")
    }

print(namesToLength)

temps = {
    "t1" : 20,
    "t2" : 25,    
    "t3" : 17,
    "t4" : 10    
    }
print(temps)

fahrenheit = {
        key: celcius*1.8 +32
        for key, celcius in temps.items()
    }
print(fahrenheit)


solution = (
    number for number in range(1,101)
    if (number %7 == 0)
    #if (number %5 != 0)
    )

sol = tuple(solution)
print(sol)
