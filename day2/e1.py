#if statement

num1 = int(input("Type a number: "))

"""num1 = input("Type  a number: ")"""

if num1 % 2 == 0:
    print(f"{num1} is even number")
    if num1 == 10:
        print(f"{num1} is ten")
    elif num1 == 6:
        print("num1 = 6")
    else:
        print("num1 != 10 y num1 !=6")
elif num1 % 2 != 0:
    print(f"{num1} is odd number")
    if num1 == 3:
        print("num1 = 3")
    elif num1 == 5:
        print("num1 = 5")
else:
    print("Invalid data")


"""pass""" 
""""Habilitar el else, pausar esa parte"""