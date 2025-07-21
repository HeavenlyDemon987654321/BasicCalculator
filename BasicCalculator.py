# Making a calculator
# Copyright 2069 Tanmay Singh
import random

insultsForOperator=["Who gave you access to a calculator??",
         "Just fcuk off of my sight!! I don't wanna see you ever again.",
         "Calling you bird brain will be insult to birds!!! YOU EXCUSE OF A HUMAN",
         "You are a burden on Earth, Please help Earth and remove that burden"]

insultsForOperand=["You can't type a single digit correctly, just go sit in Kinder Garten again",
                   "Are you actually this dumb or are just pretending to be, either way YOU ARE INSUFFERABLE",
                   "I'm pretty sure your parents will be very disappointed in you, seeing as you can't enter numbers properly."
                   "Take a bucket full of water, dunk your head in it and die of shame."]
def get_integer(prompt):
    value = input(prompt)
    if value.lower() in ["q", "quit"]:
        print("What's the point of you being here then?? Why did you even initialize the program??")
        input("Press enter to exit......")
        exit()
    if value.lower() in ["80085","69","420"]:
        print("Are you a twelve year old. Grow up already")   
    try:
        return int(value)
    except ValueError:
        print("You Goldfish. That’s not an integer. Enter something like 1, 2, 464654")
        print(random.choice(insultsForOperand))
        return None  


def get_operator(prompt):
    op = input(prompt)
    if op.lower() in ["q", "quit"]:
        print("WHY DID YOU EVEN BOTHER GIVING INPUT OPERANDS???? WASTING MY TIME OVER HERE")
        print(random.choice(insultsForOperator))
        input("Press enter to exit.....")
        exit()
    return op


while True:
    a = get_integer("Enter an operand: (Or enter q to leave) ")
    if a is None:
        continue

    b = get_integer("Enter another operand: (Or enter q to leave) ")
    if b is None:
        continue

    c = get_operator("Enter an operand (+, -, *, /), or 'q' to quit: ")

    if c == "+":
        print(f"Solution: {a + b}")
    elif c == "-":
        if a-b < 0:
            print(f"Did you actually want a negative answer? Anyway, it's: {a-b}")
        else:
             print(f"Solution: {a-b}")
    elif c == "*":
        print(f"Solution: {a * b}")
        if a == 0 or b == 0:
            print("Obviously the answer is ZERO, YOU IDIOT!! What did you think it was gonna be? You think it's a game?")
    elif c == "/":
        if b == 0:
            print("You IDIOT!!! WHY ARE YOU BEING A HERETIC???")
            continue 
        else:
            print(f"Solution: {a / b}")
    else:
        print("DO YOU EVEN KNOW WHAT THE 4 BASIC OPERANDS ARE???? IT'S EVEN INDICATED.")
        continue

    z=input("Do you wanna continue the program?(Press y or n)")
    if (z.lower()=="y"):
        continue
    else:
       print("You are capable enough to use a calculator. Okay leave now.")
       input("Press Enter to exit...")
       exit()





