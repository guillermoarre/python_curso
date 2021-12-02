def sum(x,y):
    b = x+y
    return b
sum(x=2,y=3)
#print(sum(x=2,y=3))
print(sum(2,3))


def max(a,b):
    return a>b
print(max(5,4))

x = int(input("Type a number: "))
y = int(input("Type another number: "))
if max(x,y):
    print("First number is bigger than second")
elif not max(x,y):
    print("Second number is bigger than second")
print(type(max(x,y)))