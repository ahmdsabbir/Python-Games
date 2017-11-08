import time
import random

print("Hi! I am going to assist you to survive in this haunted house.\n    But I need to know your name.\nWhat is your name?")


def ending():
    print('Good bye. I hope to see you soon!')

def running() :
    print('You ran out of the house. ')
    print('You hear footsteps behind you.')
    print( 'You realize if she catches you she will kill you.')
    print()
    print('Suddenly you saw two roads ahead.')
    print('Which one do you take? (left or right )')
    ans4 = ''
    while( ans4 != 'right' and ans4 != 'left'):
        print('choose a road.')
        ans4 = input()
    num = random.randint(1,2)
    print(name + ' you choose the ' + ans4 + ' road.')
    if( num == 1):
        print('Fortunately you have chosen the right road ' + name + '. The road leads to the aforementioned village. And you survived.')
        ending()
    elif( num == 2):
        print('Alas ' + name + '. The road you have chosen is not the correct path. You kept running for so long that you became tired.')
        print('The ghost of the witch catches you and kills you')
        ending()

def sleep_incident():
    print('you ignored the sound and continue sleeping.')
    print('Suddenly you hear a scream in the room.')
    print()
    time.sleep(5)
    print('You woke up and saw a tall dark ghost in the room')
    time.sleep(4)
    ans3 = ''
    while( ans3 != 'run') :
        print('What do you do? ')
        ans3 = input()
    if(ans3 == 'run'):
        running()

def outside_incident():
    print(name + ', you have chosen to wake up and go outside. you hear a laughter in another room. You become afraid but you decided to investigate')
    print('In that room you saw hundreds of children but no one had their head. They were all ghosts.')
    num2 = random.randint(1, 2)
    
    if(num2 == 1):
        time.sleep(3)
        print('Seeing this terrible scene you become senseless. And the witch kills you.')
        ending()
    elif( num2 == 2):
        running()


def start_game() :
    print('Let me tell you a story.')
    time.sleep(2)
    print()
    print('Once upon a time, there lived a witch in this house.')
    print('The house was in the middle of a jungle. Hardly anyone ever visited the house.')
    time.sleep(2)
    print()
    print('The witch was not a good one. She used to kidnap little boys and girls from the village nearby and brought them here. She killed those little boys and girls and drank their blood and ate their flesh.')
    time.sleep(3)
    print()
    print('But eventually the villagers found out about her.')
    print()
    print('They came to the house. And saw the witch drinking their children\'s blood')
    print()
    print('They become very angry and murdered the witch in the house')
    print()
    time.sleep(3)
    print('since then nobody ever came to this house. Because the house become haunted for ever')
    print()
    time.sleep(2)
    print(name + ' You are the only one who came to this house after that.')
    print()
    print('You were walking in the jungle and suddenly it become very dark')
    print('Then you saw this house and decided to stay in the house for the night')
    time.sleep(3)
    print()
    print()
    print('You are sleeping in the bed. It\'s midnight.')
    print('Suddenly you hear a sound.')
    print()
    print('You have two options.\n1. Keep sleeping\n2. Go outside')
    print('What do you do? (1 or 2)')
    
    ans2 = ''
    while (ans2 != '1' and ans2 != '2' ) :
        print()
        ans2 = input('Type 1 or 2 ')
    if (ans2 == '1'):
        sleep_incident()
    elif( ans2 == '2') :
        outside_incident()

name = input()

ans = ''
while (ans != 'yes' and ans != 'no'):
    print( 'Hello ' + name +'! Ready to start your adventure?')
    ans = input()

if (ans == 'no'):
    print( 'Okay ' + name + '. See you later!')
elif (ans == 'yes') :
    print('OK ' + name + '. Lets start the adventure in the Haunted House.')
    start_game()
