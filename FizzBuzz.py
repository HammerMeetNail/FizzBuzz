## If number is multiple of three, program prints "Fizz".
## If number is multiple of five, program prints "Buzz".
## If number is multiple of three and five, program prints "FizzBuzz".

## Uses for loop and modulo to evaluate multiples of 3 and 5.

def fb1():
    for i in range(1, 101):
        if i % 15 == 0:
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print 'Buzz'
        else:
            print i

## Uses while loop and modulo to evaluate multiples of 3 and 5.

def fb2():
    i = 1
    while (i <=100):
        if (i % 3 < 1 and i % 5 < 1):
            print 'FizzBuzz'
        elif (i % 3 < 1):
            print 'Fizz'
        elif (i % 5 < 1):
            print 'Buzz'
        else:
            print i
        i += 1

## Simplified for loop using slicing and modulo

def fb3():
    for i in range(1,101):
        print("Fizz"[:(i % 3 < 1) * 4] + "Buzz"[:(i % 5 < 1) * 4]) or i

## FizzBuzz in range -50 to 50 with non-negative multiples.

def fb4():
    for i in range(-50,51):
        print("Fizz"[:(i % 3 < 1 and i > 0) * 4] + "Buzz"[:(i % 5 < 1 and i > 0) * 4]) or i
