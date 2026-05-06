import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]
user_choice=int(input("what do you choose?type 0 for rock,1 for paper or 2 for scissors"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
computer_choice=random.choice(0,2)
print(f"computer chose{computer_choice}")

if user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice>user_choice:
    print("you lost")
elif computer_choice==user_choice:
    print("it is draw")
elif user_choice==computer_choice:
    print("you win")
elif computer_choice==0 and user_choice==2:
    print("you win")
else:
    print("you typed an invalid number.you lose")
    
