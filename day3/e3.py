import random
people=["Raul","Ana","Paola","Jorge","Joaquin"]

"""lucky_person = random.choice(people)
print(lucky_person)"""
#lucky_person = people[random.randint(0,4)]
lucky_person = people[random.randint(0,len(people))]
#print(lucky_person)

#Funcion split 
name_string = input("Give all the names separated by ',': ")
print(name_string)
name_list = name_string.split(',')
print(name_list)
