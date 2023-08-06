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

your_choice = int(input("Write your choice here(1 = rock, 2 = paper, 3 = scissors): "))
computer_choice = random.randint(1, 3)

if your_choice == 1:
    print(f"Your Choice:\n{rock}")
    if computer_choice == 1:
        print(f"Computer Choice:\n{rock}")
        print("Draw")
    elif computer_choice == 2:
        print(f"Computer Choice:\n{paper}")
        print("You Lose")
    elif computer_choice == 3:
        print(f"Computer Choice:\n{scissors}")
        print("You Win")
elif your_choice == 2:
    print(f"Your Choice:\n{paper}")
    if computer_choice == 1:
        print(f"Computer Choice:\n{rock}")
        print("You Win")
    elif computer_choice == 2:
        print(f"Computer Choice:\n{paper}")
        print("Draw")
    elif computer_choice == 3:
        print(f"Computer Choice:\n{scissors}")
        print("You Lose")
elif your_choice == 3:
    print(f"Your Choice:\n{scissors}")
    if computer_choice == 1:
        print(f"Computer Choice:\n{rock}")
        print("You Lose")
    elif computer_choice == 2:
        print(f"Computer Choice:\n{paper}")
        print("You Win")
    elif computer_choice == 3:
        print(f"Computer Choice:\n{scissors}")
        print("Draw")