import random
import time
hand_rules ={
        'Rock': ['Paper'],
        'Paper': ["Scissors"],
        'Scissors': ['Rock']
            }
Your_Score = 0
Ai_Score = 0
def Winner():
    if Your_Score == 3:
        print('You Win')
    else:
        print('Ai Wins')

def count():
    print("\n--- Countdown ---")
    for i in range(3, 0, -1):
        print(f'{i}...')
        time.sleep(1)
    print('reveal!\n')

def Intro():

    print("""
        Welcome to Rock, Paper, Scissors!
        In this game, you will be playing against an AI.
        The rules are simple:
        - Rock beats Scissors
        - Scissors beat Paper
        - Paper beats Rock
        It's a first to 3 match. Good luck!
        Press ENTER to start
        """)
    input()
    print('''You will be prompted to select either ROCK, PAPER, or SCISSORS.
            Afterward, a countdown will begin, revealing both your choice and the AI's selection. 
            The winner of the round will then be announced.
           '''
        )

def game():
    global Your_Score, Ai_Score
    while Your_Score < 3 and Ai_Score < 3:
        random_number = random.randint(1, 3)
        if random_number == 1:
            Bot_hand = 'Scissors'
        elif random_number == 2:
            Bot_hand = 'Paper'
        else:
            Bot_hand = 'Rock'
        Your_move = input("Your move").capitalize()

        if Your_move not in hand_rules:
           print('Please enter a valid choice')
           continue

        count()

        print("\n--- Round Result ---")
        print(f"Your choice: {Your_move}")
        print(f"AI's choice: {Bot_hand}")





        if Your_move in hand_rules[Bot_hand]:
            print("You win!")
            Your_Score += 1
            print(f"Scores -> You: {Your_Score} | AI: {Ai_Score}\n")
        elif Bot_hand in hand_rules[Your_move]:
            print('Ai wins!')
            Ai_Score +=1
            print(f"Scores -> You: {Your_Score} | AI: {Ai_Score}\n")
        else:
            print('tie')
            print(f"Scores -> You: {Your_Score} | AI: {Ai_Score}\n")
            print("----------------------\n")



Intro()
game()
Winner()
