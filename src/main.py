import os
import colorama
import time
from colorama import Fore, Style
from utils import clear
from questions import easy_questions, medium_questions, hard_questions
import random

colorama.init(autoreset=True)

def display_banner():
    print(Fore.RED + Style.BRIGHT + """
      _____     __           ____               __ 
     / ___/_ __/ /  ___ ____/ __/_ _  ___ _____/ /_
    / /__/ // / _ \/ -_) __/\ \/  ' \/ _ `/ __/ __/
    \___/\_, /_.__/\__/_/ /___/_/_/_/\_,_/_/  \__/ 
        /___/                                      
    """)
    print(Fore.CYAN + Style.BRIGHT + """
       ______           __    ____       _   
      / __/ /____ _____/ /_  / __ \__ __(_)__
     _\ \/ __/ _ `/ __/ __/ / /_/ / // / /_ /
    /___/\__/\_,_/_/  \__/  \___\_\_,_/_//__/
    """)
    print(Fore.GREEN + Style.BRIGHT + "-" * 60)

def display_description():
    print(Fore.CYAN + "-" * 70)
    print(Fore.BLUE + Style.BRIGHT + "Welcome to the CyberSmart Start Quiz! Let's learn about online safety.")
    print(Fore.CYAN + "-" * 70)

def get_user_input():
    clear()
    display_banner()
    display_description()

    name = input(Fore.YELLOW + Style.BRIGHT + "Please enter your name: " + Fore.RESET).strip()
    while not name:
        clear()
        display_banner()
        display_description()
        name = input(Fore.YELLOW + "Name is required. Please enter your name: " + Fore.RESET).strip()

    age = input(Fore.YELLOW + Style.BRIGHT + "Please enter your age: " + Fore.RESET).strip()
    while not age.isdigit():
        clear()
        display_banner()
        display_description()
        age = input(Fore.YELLOW + "Age is required and must be a number. Please enter your age: " + Fore.RESET).strip()

    age = int(age)
    if age >= 14:
        clear()
        display_banner()
        display_description()
        print(Fore.YELLOW + "You're 14 or older! You might want to try the CyberSmart Youth Quiz instead.")
        time.sleep(1)
        
        while True:
            print(Fore.YELLOW + Style.BRIGHT + "Do you still want to proceed with this quiz? (y/n)")
            proceed = input(Fore.GREEN + "> " + Fore.RESET).strip().lower()

            if proceed in ["y", "yes"]:
                break
            elif proceed in ["n", "no"]:
                print(Fore.BLUE + Style.BRIGHT + "Okay, feel free to try the CyberSmart Youth Quiz!")
                exit()
            else:
                clear()
                display_banner()
                display_description()
                print(Fore.RED + "Invalid choice. Please enter 'y' or 'n'.")

    return name

def select_mode():
    while True:
        clear()
        display_banner()
        print(Fore.CYAN + Style.BRIGHT + "Select Difficulty Mode:")
        print(Fore.GREEN + "1. Easy (10 questions)")
        print(Fore.YELLOW + "2. Medium (20 questions)")
        print(Fore.RED + "3. Hard (30 questions)")
        mode = input(Fore.CYAN + "Enter the number of the mode you want to play: " + Fore.RESET).strip()

        if mode == "1":
            return easy_questions
        elif mode == "2":
            return medium_questions
        elif mode == "3":
            return hard_questions
        else:
            clear()
            display_banner()
            print(Fore.RED + "Invalid selection. Please choose 1, 2, or 3.")

def run_quiz(questions, name):
    score = 0
    total_questions = len(questions)

    for i, q in enumerate(random.sample(questions, len(questions))):
        attempts = 3
        while True:
            clear()
            display_banner()
            print(Fore.CYAN + f"{name}'s Quiz")
            print(Fore.GREEN + f"Score: {score} | Attempts: {attempts} | Progress: {i+1}/{total_questions}")
            print(Fore.MAGENTA + q["question"])

            for option in q["options"]:
                print(Fore.YELLOW + option)

            answer = input(Fore.CYAN + "Your answer (1-4): " + Fore.RESET + Fore.YELLOW + Style.BRIGHT).strip()

            if not answer.isdigit() or not 1 <= int(answer) <= 4:
                clear()
                display_banner()
                continue

            if int(answer) == q["correct_answer"]:
                if attempts == 3:
                    score += 1
                print(Fore.GREEN + "Correct!")
                input(Fore.CYAN + "Press Enter to continue..." + Fore.RESET)
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print()
                else:
                    print(Fore.RED + f"Incorrect. The correct answer was {q['correct_answer']}.")
                    input(Fore.CYAN + "Press Enter to continue..." + Fore.RESET)
                    break

    while True:
        clear()
        display_banner()
        print(Fore.CYAN + f"Quiz Complete, {name}!")
        print(Fore.GREEN + f"Final Score: {score}/{total_questions}")
        print(Fore.CYAN + "Would you like to play again or exit?")
        print(Fore.GREEN + "1. Play Again")
        print(Fore.RED + "2. Exit")

        choice = input(Fore.CYAN + "Enter your choice (1-2): " + Fore.RESET).strip()
        if choice == "1":
            questions = select_mode()
            run_quiz(questions, name)
        elif choice == "2":
            print(Fore.CYAN + "Thank you for playing! Stay safe online.")
            exit()
        else:
            clear()
            display_banner()

def main():
    try:
        clear()
        display_banner()
        display_description()
        time.sleep(0.5)
        
        name = get_user_input()
        questions = select_mode()
        run_quiz(questions, name)

    except KeyboardInterrupt:
        while True:
            clear()
            display_banner()
            print(Fore.RED + "Are you sure you want to quit? (y/n)")
            choice = input(Fore.GREEN + "> " + Fore.RESET).strip().lower()

            if choice in ["y", "yes"]:
                print(Fore.CYAN + "Thank you for playing! Stay safe online.")
                exit()
            elif choice in ["n", "no"]:
                main()
            else:
                clear()
                display_banner()

if __name__ == "__main__":
    main()

