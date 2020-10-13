import random

a = ['ROCK', 'SPOCK', 'PAPER', 'LIZARD', 'SCISSORS']
pc = 0
cc = 0
count = 1
rp = 0
rc = 0

def name_to_number(name):
    x = -1
    if name in a:
        pass
    else:
        print ("Error: Invalid option")
        print ("Restarting Game...")
        rpsls(pc, cc, count, rc, rp, n)
    for i in range(len(a)):
        if name == a[i]:
            x = i
    return x

def number_to_name(number):
    y = ''
    if number in range(len(a)):
        pass
    else:
        print("Error: Out of range")
        exit()
    for i in range(len(a)):
        if number == i:
            y = a[number]
    return y

def rpsls(pc, cc, count, rc, rp, n): 
            
    print ('\n')
    player_choice = input('Enter your choice: ')
    player_choice = player_choice.upper()
    if player_choice != 'QUIT':
        print ("Round = ",count)
        if count < n+1:
            if pc < 5 and cc < 5:
                print('Player chooses ',player_choice)
                player_number = name_to_number(player_choice)
                comp_number = random.randrange(0,4)
                comp_choice = number_to_name(comp_number)
                print('Computer chooses ',comp_choice)
                diff = player_number - comp_number
                if diff%5 == 0:
                    print("It's a tie !")
#                    rpsls(pc, cc, count, rc, rp)
                elif diff%5 >= 3:
                    print("Computer wins!")
                    cc+=1
                    print("Player = ", pc, "Computer = ", cc, "Round =",count)
#                    rpsls(pc, cc, count, rc, rp)
                elif diff%5 <= 2:
                    print("Player wins!")
                    pc+=1
                    print("Player = ", pc, "Computer = ", cc, "Round =",count)
#                    rpsls(pc, cc, count, rc, rp)
            if pc == 5:
                  rp+=1
                  print("Round ", count, ": Player wins !")
                  count+= 1
                  pc = 0
                  cc = 0
                 # rpsls(pc, cc, count, rc, rp)
            if cc == 5:
                  rc+=1
                  print("Round ", count, ": Computer wins !")
                  count+= 1
                  pc = 0
                  cc = 0
           
        if count == n+1:
            print("Score Board:")
            print("Player score: ", rp, "Computer Score: ", rc)
            if rp > rc:
                print("Game over ! Player wins !")
                exit()
            elif rp < rc :
                print("Game over ! Computer wins !")
                exit()
            else:
                print("Whoops ! It's a tie !")
                r = input('Would you like to play a super-round ? Yes/No: ')
                if r.upper() == 'YES':
                    count = 1
                    rpsls(pc, cc, count, rc, rp, 1)
                else:
                    exit()
                    
        else:
            rpsls(pc, cc, count, rc, rp, n)
    else:
        exit()

#MAIN PROGRAM
print("Rock-Paper-Scissors-Lizard-Spock Challenge")
print("It's very simple:\nScissors cuts paper, paper covers rock,\nrock crushes lizard, lizard poisons Spock,\nSpock smashes scissors, scissors decapitate lizard,\nlizard eats paper, paper disproves Spock,\nSpock vaporizes rock. And as it always has, rock crushes scissors.\n\t\t~Dr. Sheldon Cooper")
diff = 0
n = int(input('How many rounds to play ?'))
if n == 0:
    print('Too low')
    exit()
else:
    while True:
        rpsls(pc, cc, count, rc, rp, n)