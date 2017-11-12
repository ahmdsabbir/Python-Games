import random

def start():
    print('*******************************************************************')
    print()
    print('                     G U E S S                                  ')
    print('                       T H E                                 ')
    print('                    N U M B E R                           ')
    print()
    print('********************************************************************')

start()

name = input('What is you name? ')


print('*************************************************************************')
print()
print('                       H E L L O O O O                                   ')
print()
print('                         ' + name + '                               ')
print()
print('**************************************************************************')

def won():
    print('****************************************************************************')
    print('*******************                            *****************************')
    print('                    C O N G R A T U L A T I O N                             ')
    print('*******************                            *****************************')
    print('****************************************************************************')

def lost():
    print('****************************************************************************')
    print('*******************                            *****************************')
    print('                       Y O U   L O S T                             ')
    print('*******************                            *****************************')
    print('****************************************************************************')

def game() :
    num = random.randint(1,20)
    print()
    print('Guess a number between 1 and 20.')
    guess = input()

    if( guess == num):
        won()
    else:
        tries = 0
        while(guess != num and tries <= 4):

            print()
            guess = input('Not Correct! Try again ' + name + ': ')

            if(int(guess) < num):
                print()
                print(name + ' -------- guess higher--------------.')
            elif(int(guess) > num):
                print()
                print(name + '-------- guess lower------------------')

            if(guess == str(num)):
                won()
                print(name + ' You won! the number is ' + str(num) + '\nAnd it took ' + str(tries) + '.')
                break
            if(tries == 4):
                lost()

            if(tries == 2):
                print()
                print(name + ' you have only two tries left')
            if(tries == 3):
                print()
                print(name + ' you have only one try left')
            if(tries == 1):
                print()
                print(name + ' you have only three tries left')

            tries = tries+1


ans = ''
 
while(ans != 'yes' and ans != 'no') :
    print('Are you ready?')
    ans = input()

if( ans == 'no') :
    print('Ok, ' + name + ' See you next time!')

else:
    game()
