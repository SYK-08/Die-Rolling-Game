import random
i = input('Would you like to roll a die?(y/n):')
if i=='n':
    print('Oh, okay.')
elif i=='y':
    print('Ok lets go then!')
    print('Now, type ''toss'' below to get your number' )
    die = input('Type here: ')
    if die=='toss':
        random_number = random.randint(1,6)
        print('And your number is: '+ str(random_number))
