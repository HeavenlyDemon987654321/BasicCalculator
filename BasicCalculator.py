# Making a calculator
# Copyright 2069 Tanmay Singh
import random

insultsForOperator=["Who gave you access to a calculator??\n",
                    "Just fcuk off of my sight!! I don't wanna see you ever again.\n",
                    "Calling you bird brain will be insult to birds!!! YOU EXCUSE OF A HUMAN\n",
                    "You are a burden on Earth, Please help Earth and remove that burden\n"]

insultsForOperand=["You can't type a single digit correctly, just go sit in Kinder Garten again\n",
                   "Are you actually this dumb or are just pretending to be, either way YOU ARE INSUFFERABLE\n",
                   "I'm pretty sure your parents will be very disappointed in you, seeing as you can't enter numbers properly.\n",
                   "Take a bucket full of water, dunk your head in it and die of shame.\n"]
def get_integer(prompt):
    value = input(prompt)
    if value.lower() in ["q", "quit"]:
        print("What's the point of you being here then?? Why did you even initialize the program??\n")
        input("Press enter to exit......\n")
        exit()
    if value.lower() in ["80085","69","420"]:
        print("Are you a twelve year old??? Grow up already...\n")   
    try:
        return int(value)
    except ValueError:
        print("You Goldfish. That’s not an integer. Enter something like 1, 2, 464654....\n")
        print(random.choice(insultsForOperand))
        return None  


def get_operator(prompt):
    op = input(prompt)
    if op.lower() in ["q", "quit"]:
        print("WHY DID YOU EVEN BOTHER GIVING INPUT OPERANDS???? WASTING MY TIME OVER HERE...\n")
        print(random.choice(insultsForOperator))
        input("Press enter to exit.....")
        exit()
    return op


while True:
    a = get_integer("Enter an operand (Or enter q to leave): ")
    if a is None:
        continue

    b = get_integer("Enter another operand (Or enter q to leave): ")
    if b is None:
        continue

    c = get_operator("Enter an operand (+, -, *, /), or 'q' to quit: ")

    if c == "+":
        d=a+b
        print(f"Solution: {d}\n")
    elif c == "-":
        d=a-b
        if d < 0:
            print(f"Did you actually want a negative answer? Anyway, it's: {d}\n")
        else:
             print(f"Solution: {d}\n")
    elif c == "*":
        d=a*b
        print(f"Solution: {d}\n")
        if a == 0 or b == 0:
            print("Obviously the answer is ZERO, YOU IDIOT!! What did you think it was gonna be? You think it's a game?\n")
    elif c == "/":
        if b == 0:
            print("You IDIOT!!! WHY ARE YOU BEING A HERETIC??? DON'T YOU KNOW YOU CAN'T DO THAT AND DON'T ASK WHY\n")
            continue 
        else:
            d=a/b
            print(f"Solution: {d}\n")
    else:
        print("YOU IDIOT!!!!DO YOU EVEN KNOW WHAT THE 4 BASIC OPERANDS ARE???? IT'S EVEN INDICATED.\n")
        continue
    if (len(str(d))<=3 or len(str(a))<=3 or len(str(b))<=3):
        print("You are asking such an easy fcuking question, are you actually a 12 year old or an adult with a stunted brain?? RETARD!!!\n")



    z=input("Do you wanna continue the program?(Press y or n)")
    if (z.lower()=="y"):
        continue
    elif z.lower() not in ["y","n"]:
        print("ALL YOU HAD TO IS JUST TYPE Y OR N, and you bloody idiot can't fcuking do that!!!!! If this is done intentionally, I swear to GOD, IF I HAD A HUMAN BODY... I WOULD'VE STARTED HITTING YOU WITH A FUCKING CRICKET BAT\n")    
    else:
       print("You are capable enough to use a calculator. Okay leave now.")
       input("Press Enter to exit...")
       exit()






