#Homework_1 LEAP-YEAR
#A year is a LY if it can be divided by 4
#except if it can be divided by 100
#the last have a excpetion if it can be divided by 400

anio = int(input("Type a year: "))

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print(f"{anio} is a LeapYear")
        else:
            print(f"{anio} is not a LeapYear")
    else:
        print(f"{anio} is a LeapYear")
else:
    print(f"{anio} is not a LeapYear") 