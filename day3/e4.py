#piedra, papel o tijera
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
computer =random.randint(0,len(game)-1)
choice = int(input("Make a choice 0-rock, 1-paper, 2-scissors: "))
#print(game[choice])

if choice == 0 and computer == 2:
    print("User wins!!")
elif choice == 2 and computer == 0:
    print("Computer wins!!")
elif choice == computer:
    print("It is a tie!!")
elif choice > computer:
    print("User wins!!")
elif choice < computer:
    print("Computer wins!!")
#Print
print("User's choice: ")
print(game[choice])
print("Computer's choice: ")
print(game[computer])
