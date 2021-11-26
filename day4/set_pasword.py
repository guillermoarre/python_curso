import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator")
n_letters = int(input("How many letters would ou like your password?: "))
n_numbers = int(input("How many numbers would ou like your password?: "))
n_symbols = int(input("How many symbols would ou like your password?: "))

#easy way 
password = ""
for cicle in range(1,n_letters+1):
    password += random.choice(letters)
for _ in range(1,n_numbers+1):
    password += random.choice(numbers)
for _ in range(1,n_symbols+1):
    password += random.choice(symbols)

#print(f"Password: {password}")

#hard_way
password_list = []
for _ in range(1,n_letters+1):
    password_list.append(random.choice(letters))
for _ in range(1,n_numbers+1):
    password_list.append(random.choice(numbers))
for _ in range(1,n_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(f"Password: {password_list}")
string_list_password = ""
for _ in password_list:
    string_list_password += _
print(f"Password: {string_list_password}")