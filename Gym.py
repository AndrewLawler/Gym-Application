# Main Project
# Gym Application
# Andrew - 07/02/19

import random

#Main Arrays
Arms = ["Bicep Curl", "Concentration Curl", "Hammer Curl", "Cable Curl", "Tricep Pushdown", "Skull Crusher", "Cable Tricep Pulldown", "Rope Pushdown", "Tricep Extension", "Overhead Press", "Arnold Press", "Lateral Raise", "Rear Delt Machine Fly", "Delt Cable Pull", "Dumbell Shoulder Press"]
Chest = ["Bench Press", "Cable Fly", "Machine Fly", "Machine Chest Press", "Dumbell Press"]
Back = ["Deadlift", "Row", "Bent Over Row", "Wide-Grip Pull-Up", "Standing T-Bar Row", "Single Dumbell Row", "Lat Pulldown"]
Legs = ["Squat", "Calf Raise", "Smith Machine Calf Raise", "Leg Press", "Leg Extension", "Leg curl"]
Abs = ["Crunch", "Roman Twist", "Plank"]

Bicep = Arms[0:4]
Tricep = Arms[4:9]
Shoulder = Arms[10:14]

Body = Arms+Chest+Back+Legs+Abs

def Main():
    print(Bicep)
    print("Welcome to Gym Application!")
    Menu = input("\nWould you like to do a full body workout or simply get exercises for specific parts? FB or SP: ")
    Menu = Menu.upper()
    print()
    if Menu == "FB":
        fullBody()
    elif Menu == "SP":
       specificPart()
    else:
        Main()


def fullBody():
    #in
    Sets = int(input("How Many Sets?: "))
    Exercises = int(input("How Many Exercises?: "))

    print()

    x = 1 # Loop for exercises
    i = 1 # Loop for sets
    exerciseNumber = 0 # List Variable

    while i<=Sets:
        print("Day:",i,"\n")
        i = i+1
        while x<=Exercises:
            x = x+1
            exerciseNumber = exerciseNumber + 1
            num = random.randint(0,30)
            print(exerciseNumber,Body[num])
        exerciseNumber = 0
        x = 1
        print()
    Main()

def specificPart():
    #in
    Part = input("Body Part?: ")
    Part = Part.lower()
    a = 1
    c = 0
    if Part == "shoulder":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,5)
            print(c,Shoulder[s])
    elif Part == "tricep":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,4)
            print(c,Tricep[s])
    elif Part == "bicep":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,3)
            print(c,Bicep[s])
    elif Part == "chest":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,4)
            print(c,Chest[s])
    elif Part == "back":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,6)
            print(c,Back[s])
    elif Part == "legs":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,5)
            print(c,Legs[s])
    elif Part == "abs":
        Amount = int(input("How Many Exercises?: "))
        while a<=Amount:
            c = c + 1
            s = random.randint(0,2)
            print(c,Abs[s])
    else:
        print("Please Enter a body part.")
        print("\nTry Again")
        specificPart()    
    Main()
Main()


    
