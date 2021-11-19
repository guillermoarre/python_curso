import random #libreria random

"""list1 = [12,0,3,True,'hello']
#print(list1[0])
print(random.choice(list1))
#Elige un dato aleatoria de la lista

var = random.randint(1,100)
print(var)"""

coin = ["head","tails"]

if random.choice(coin) == "head":
    print("head")
elif random.choice(coin) == "tails":
    print("tails")
    