#HW
#3-5 fizzbuzz
#3 fizz
#5 buzz
num = int(input("Type a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0  and num % 5 != 0:
    print("fizz")
elif num % 3 != 0 and num % 5 == 0:
    print("buzz")
else:
    print("nop")
    