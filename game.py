'''
This program is for playing " stone paper scissor game " by taking
choice from users and can also make random choice of computer and
detect the winners.
'''
#!/user/bin/env python3

import sys
import subprocess
import random

def menu():
    tmp=subprocess.call('clear',shell=True)
    print('....................................................')
    print('Program to play stone, paper, scissor game.')
    print('....................................................')
    print("s.START")
    print('x.END')
    print('....................................................')
    print('Enter the choice :',end='')
    choice=input().lower()
    return choice

def selection_menu(name):
    tmp=subprocess.call('clear',shell=True)
    print("for {}......".format(name))
    print('.....................................................')
    print('s.stone')
    print('p.paper')
    print('c.scissor')
    print("d.Back")
    print('.....................................................')
    print('Enter the choice :',end='')
    selection = input().lower()
    return selection

def get_computerchoice(l):
    computerChoice = random.choice(l)
    print('Computer Choice :',computerChoice)
    return computerChoice

def getResult(playerChoice,userChoice,l,name):
    if userChoice == playerChoice:
        result='TIE!!!'
    else :
        for i in range(len(l)):
            if userChoice == l[i]:
                if (i+1)<len(l):
                    if playerChoice == l[i+1]:
                        result ='User Wins!!!'
                    else:
                        result ='{} wins!'.format(name)
                else :
                    if playerChoice == l[0]:
                        result='User Wins!!!'
                    else:
                        result='{} wins!'.format(name)

    return result

def selection_of_players():
    tmp=subprocess.call('clear',shell=True)
    print("................................")
    print("Who would you like to play with?")
    print("A.Computer")
    print("B.Another player")
    print("C.Back")
    print("................................")
    print("Enter the choice : ",end = "")
    player_choice = input().upper()
    return player_choice

def get_playerChoice(player_selection,l):
    if player_selection == 'A':
       playerChoice = get_computerchoice(l)
       name = "Computer"

    if player_selection == 'B':
       playerChoice = selection_menu("player")
       name = "Player"
    return playerChoice,name

def game(userChoice,player_selection):
    l=['stone','scissor','paper']
    while True:
        playerChoice,name = get_playerChoice(player_selection,l)

        if userChoice == 's':
            user_choice = l[0]
            print('User Choice :',user_choice)

        if userChoice == 'c':
            user_choice = l[1]
            print('User Choice :',user_choice)

        if userChoice == 'p':
            user_choice = l[2]
            print('User Choice :',user_choice)

        if name != "Computer":
            if playerChoice == 's':
                player_choice = l[0]
                print(name ,' Choice :',player_choice)

            if playerChoice == 'c':
                player_choice = l[1]
                print(name ,' Choice :',player_choice)

            if playerChoice == 'p':
                player_choice = l[2]
                print(name ,' Choice :',player_choice)
        else:
             player_choice = playerChoice

        con=input('continue......')
        result = getResult(player_choice,user_choice,l,name)
        return result

def displayresult(result):
    print("\nThe Result is ..............")
    print(result)
    waite = input()

def main():
    while True:
        choice = menu()
        if choice == 's':
            player_selection = selection_of_players()
            if player_selection == 'C': choice = menu()
            else:
                selection = selection_menu("user")
                if selection == 'd': selection = selection_of_players()
                else:
                    input("......")
                    result = game(selection,player_selection)
                    displayresult(result)

        if choice == 'x':
            print('Thank YOU !!!🙏️')
            print('..............................................')
            sys.exit(0)

        print()
if __name__=='__main__':
    main()
