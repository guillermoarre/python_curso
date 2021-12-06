
from art import logo
alphabet = ['a', 'b', 'c', 'd',' ', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c'," ", 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c'," ", 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(selection,shift,start_text):
    end_text = ''
    if selection == 'decode':
        shift *= -1

    for _ in start_text:
        if _ in alphabet:
            position=alphabet.index(_)
            new_position = position + shift
            end_text = end_text + alphabet[new_position] 
            #Concatenar letras 
    return end_text
    
print(logo)
flag = False

while not flag:
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    shift = int(input("Type the shift number: "))
    text = input("Type your message: ").lower()
    print(caesar(selection,shift,text))

    if input("Type 'yes' if you want to go again. Otherwise type 'no': ") == 'no':
        flag = True
print("Good bye")


