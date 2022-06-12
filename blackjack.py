import random
import os
from time import sleep
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
user_point = []
computer_cards = []
computer_point = []
end_game = False

def new_game():
    print(logo)
    user_cards.clear()
    user_point.clear()
    computer_cards.clear()
    computer_point.clear()


def cls():
    sleep(0)
    os.system('cls')


def deal_user():
    id = random.randint(0, 12)
    user_cards.append(cards[id])
    user_point.append(points[id])


def deal_computer():
    id = random.randint(0, 12)
    computer_cards.append(cards[id])
    computer_point.append(points[id])


def calc_point(points):
    if sum(points) == 21 and len(points) == 2:
        return 0
    if 11 in points and sum(points) > 21:
        points.remove(11)
        points.append(1)
    return sum(points)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def final(user_score, computer_score):
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

def current(user_score):
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")


def play_game():
    cls()
    new_game()
    for _ in range(0, 2):
        deal_user()
        deal_computer()
    
    end_game = False
    user_score = calc_point(user_point)
    computer_score = calc_point(computer_point)
    current(user_score)
    if user_score == 0:
        print(compare(user_score, computer_score))
    else:
        while not end_game:
            while user_score < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                deal_user()
                user_score = calc_point(user_point)
                current(user_score)
            end_game = True
            if user_score > 21:
                final(user_score, computer_score)
                print(compare(user_score, computer_score))
            else:
                while calc_point(computer_point) < 17:
                    deal_computer()
                    computer_score = calc_point(computer_point)
                final(user_score, computer_score)
                print(compare(user_score, computer_score))

while input("Do you want to play a game blackjack? Type 'y' or 'n': ") == "y":
    play_game()
