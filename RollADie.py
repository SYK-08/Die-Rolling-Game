import random

i = input('Would you like to roll a die?(y/n):').lower()

def rolladie():
    if i == "y":
        random_number = random.randint(1,6)
        print('And your number is: '+ str(random_number))
    elif i == "n":
        exit()

def again():
    while True:
        i2 = input("Would you like to roll a die again?(y/n)").lower()
        if i2 == "y":
            rolladie()
        elif i2 == "n":
            exit()

rolladie()
again()
