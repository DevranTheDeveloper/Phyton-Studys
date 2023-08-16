import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

def card_randomizer():
    # Draw two random cards for the player and the computer
    for _ in range(2):
        random_card = random.choice(cards)
        your_cards.append(random_card)
        random_card = random.choice(cards)  # Get a new random card for the computer
        computer_cards.append(random_card)
    
    print(f"Your cards are: {your_cards}. \nYour score is: {sum(your_cards)}")
    print(f"Computer's first card is: {computer_cards[0]}")
    

def chit(cards):
    total_score = sum(cards)
    if total_score > 21:
        return "Bust"
    elif total_score == 21:
        return "Blackjack"
    return None
    
def add_card(cards):
    random_card = random.choice(cards)
    cards.append(random_card)
    return cards

play = input("Do you want to play a Blackjack game (y,n)?: ")

if play == "y":
    card_randomizer()
    hit = input("Do you want to hit a card or stand (h,s)?: ")
    
    while hit == "h":
        your_cards = add_card(your_cards)
        print(f"Your cards are: {your_cards}. \nYour score is: {sum(your_cards)}")
        result = chit(your_cards)
        if result == "Bust":
            print("Bust! You Lose.")
            break
        elif result == "Blackjack":
            print("Blackjack! You Win.")
            break
        hit = input("Do you want to hit a card or stand (h,s)?: ")
    
    if hit == "s":
        while sum(computer_cards) < 17:
            computer_cards = add_card(computer_cards)
        
        print(f"Computer's cards are: {computer_cards}. \nComputer's score is: {sum(computer_cards)}")
        
        player_result = chit(your_cards)
        computer_result = chit(computer_cards)
        
        if player_result == "Bust":
            print("You Bust! Computer Wins.")
        elif computer_result == "Bust":
            print("Computer Busts! You Win.")
        elif player_result == "Blackjack":
            print("Blackjack! You Win.")
        elif computer_result == "Blackjack":
            print("Computer has Blackjack. Computer Wins.")
        elif sum(your_cards) > sum(computer_cards):
            print("You Win!")
        elif sum(your_cards) < sum(computer_cards):
            print("Computer Wins!")
        else:
            print("It's a Tie!")
else:
    print("Game Ended")

    
    
