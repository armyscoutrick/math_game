import random
import os

def clear():
    os.system("clear")  

def start_game():
    clear()
    print("Welcome to Math Flashcards!")
    operations = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
    choice = input("Choose your flashcards (add|subtract|multiply|divide): ").lower()

    if choice in operations:
        flashcard_loop(operations[choice])
    else:
        print(f"Sorry, I don't recognize '{choice}'")
        input("Press Enter to try again...")
        start_game()

def generate_problem(op):
    if op == "/":
        a, b = random.randint(0, 10), random.randint(1, 10)
        result = round(a / b, 2)
    elif op == "-":
        a, b = sorted([random.randint(0, 10), random.randint(0, 10)], reverse=True)
        result = a - b
    elif op == "+":
        a, b = random.randint(0, 10), random.randint(0, 10)
        result = a + b
    elif op == "*":
        a, b = random.randint(0, 10), random.randint(0, 10)
        result = a * b
    return a, b, result

def flashcard_loop(op):
    clear()
    a, b, correct = generate_problem(op)

    if op == "/":
        answer = input(f"{a} / {b} (rounded to 2 decimal places): ")
        try:
            if round(float(answer), 2) == correct:
                print(f"Correct! {a} / {b} = {correct:.2f}")
            else:
                print(f"Wrong! {a} / {b} = {correct:.2f}")
        except ValueError:
            print("Invalid input. Expected a decimal number.")
    else:
        answer = input(f"{a} {op} {b}: ")
        try:
            if int(answer) == correct:
                print(f"Correct! {a} {op} {b} = {correct}")
            else:
                print(f"Wrong! {a} {op} {b} = {correct}")
        except ValueError:
            print("Invalid input. Expected an integer.")

    next_action = input("Would you like another card? (yes|no|restart): ").lower()
    if next_action == "yes":
        flashcard_loop(op)
    elif next_action == "no":
        print("Thanks for playing!")
    elif next_action == "restart":
        start_game()
    else:
        print(f"Sorry, I don't recognize '{next_action}'")
        input("Press Enter to try again...")
        flashcard_loop(op)

if __name__ == "__main__":
    start_game()
