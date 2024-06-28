import random
import sys

def generate_secret_number(min_num, max_num):
    return random.randint(min_num, max_num)

def get_user_guess(min_num, max_num):
    while True:
        try:
            guess = int(input(f"Enter your guess ({min_num} - {max_num}):"))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"please enter a number between {min_num} and {max_num}")
        except ValueError:
            print("Invalid input! Please enter a valid number")

def get_range_from_user():
    while True:
        try:
            min_num = int(input("Enter the minimum number for the range:"))
            max_num = int(input("Enter the maximum number for the range:"))
            if min_num >= max_num:
                print("Minimum number should be less than maximum number:")
            else:
                return min_num, max_num
        except ValueError:
            print("Invalid input! Please enter valid integers")

def get_attempts():
    while True:
        try:
            attempts = int(input("Enter the number of attempts (1-10):"))
            if 1 <= attempts <= 10:
                return attempts
            else:
                print("Please enter a number between 1 and 10")   
        except ValueError:
            print("Invalid input! Please enter a valid number")

def play_game():
    print("Welcome to the Number Guessing Game!")
    min_num, max_num = get_range_from_user()
    secret_number = generate_secret_number(min_num, max_num)
    attempts_left = get_attempts()
    score = 100
    hints_used = 0

    print(f"Im thinking of a number between {min_num} and {max_num}")

    while attempts_left > 0:
        print("\n Attempts left:", attempts_left)
        guess = get_user_guess(min_num, max_num)
        
        if guess < secret_number:
            print("Too Low! Try a Higher Number")
        elif guess > secret_number:
            print("Too High! Try a Lower Number")    
        else:
            print(f"Congradualations! You guessed the number {secret_number} correctly!")
            print(f"Your score is: {score}")   
            if score > 0:
                update_high_score(score)
                break

            attempts_left -= 1
            score -= 10

            if attempts_left > 0:
                use_hint = input("Would you like a hint? (yes/no):").lower()
                if use_hint == "yes":
                    hints_used +=1
                    give_hint(guess, secret_number, min_num, max_num)

    if attempts_left == 0:
        print(f"\n Game Over! The secret number was {secret_number}. Better luck next time!")

        print(f"\n Hints used: {hints_used}")
        print_high_scores()       

        Play_again =input("Do you want to play again? (yes/no):").lower()
        if Play_again == "yes":
            play_game()
        else:
            print("Thank you for playing!")

def give_hint(guess, secret_number, min_num, max_num):
    midpoint =(min_num + max_num) // 2
    if guess < secret_number:
        if guess < midpoint:
            print("Hint: Try guessing a bit higher")
        else:
            print("Hint: You're very close! Try a slightly higher number")  
    else:          
        if guess > midpoint:                       
            print("Hint: Try guessing a bit lower")
        else:
            print("Hint: You're very close! Try a slightly lower number")     

high_scores = []

def update_high_score(score):
    global high_scores
    high_scores.append(score)
    high_scores.sort(reverse=True)
    if len(high_scores) >5:
        high_scores = high_scores[:5]

def print_high_scores():
    global high_scores
    if high_scores:
        print("\n High Scores:")
        for i, score in enumerate(high_scores,start=1):
            print(f"{i}. Score: {score}") 
    else:
        print("\n No High scores yet. Be the First one!")

if __name__ == "__main__":
    play_game()      

    



                









