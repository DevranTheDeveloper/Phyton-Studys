#number guess
import random
number = random.randint(1,101)

def easy():
    hak = 10
    while True:
        guess = int(input("Guess a Number: "))
        if guess > number:
            print("Too High Guess Again.")
            hak -= 1
            print(f"{hak} hak remain.")
            
        elif guess < number:
            print("Too Low Guess Again.")
            hak -= 1
            print(f"{hak} hak remain.")
            
        elif guess == number:
            print("Correct. You Win !!")
            break
        if hak == 0:
            print("Hakkın bitti çevirmeye üşendim.")
            break
        
def hard():
    hak = 5
    while True:
        guess = int(input("Guess a Number: "))
        if guess > number:
            print("Too High Guess Again.")
            hak -= 1
            print(f"{hak} hak remain.")
            
        elif guess < number:
            print("Too Low Guess Again.")
            hak -= 1
            print(f"{hak} hak remain.")
            
        elif guess == number:
            print("Correct. You Win !!")
            break
        if hak == 0:
            print("Hakkın bitti çevirmeye üşendim.")
            break 

print("Welcome to the Number Guess game.")
print("I'm thinking of a number between 1 and 100.")
diff = input("Choosa a difficulty. Type 'easy' or 'hard': ").lower()

if diff == "easy": 
    easy()
elif diff == "hard": 
    hard()   
else: 
    print("Input a valid variable.")


