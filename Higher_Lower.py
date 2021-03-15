import random
from art import *
from data import *


program_on = True
game_on = True
score = 0
print(logo)


person_a = random.choice(data)
while program_on:
    while game_on:
        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
        print(vs + "\n")
        person_b = random.choice(d.data)
        while person_b == person_a:
            person_b = random.choice(d.data)
        print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_a['country']}.")
        guess = input("Who has more followers? 'a' or 'b' ")
        if person_a['follower_count'] > person_b['follower_count']:
            winner = 'a'
        else:
            winner = 'b'

        if guess == winner:
            score += 1
            print(f"You are correct. Your score is {score}.")
            person_a = person_b
        else:
            game_on = False
            print(f"Incorrect. Your final score was {score}.")
    score = 0
    if input("Do you want to play again? ") == "yes":
        game_on = True
    else:
        program_on = False
