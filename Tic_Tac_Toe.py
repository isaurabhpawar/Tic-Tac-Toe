"""
This is created by saurabh pawar.
As an attemp to create Tic Tac Toe,
the classic paper pencil game in as a python developed computer game.
"""
import random                   #To select random number
board = [" "] * 9               # Initalise empty spaces for the tic-tac-toe board
avail_choices = [0,1,2,3,4,5,6,7,8] #Create a list for the availabe choices for computer selection


#Create a function to draw an 3X3 tic-tac-toe board
def draw_board(board):
    row_1 = '{}|{}|{}'.format(board[0], board[1], board[2])
    row_2 = '{}|{}|{}'.format(board[3], board[4], board[5])
    row_3 = '{}|{}|{}'.format(board[6], board[7], board[8])

    print(row_1 + '\n' + row_2 + '\n' + row_3 + '\n')

#Create a function to take a input on dezired locaton from user
def user_move(board,user_type):
    user_choice = int(input("Choose your space between 1-9: ")) - 1
    if board[user_choice] != " ":
        print ("Space is already taken by {}".format(board[user_choice]))
        user_move(board, user_type)
    else:
        board[user_choice] = user_type
        avail_choices.remove(user_choice)
        draw_board(board)


#Create a function to randomly make an move by computer
def comp_move(board, user_type):
    print("Computer's Move")
    comp_choice = random.choice(avail_choices)
    avail_choices.remove(comp_choice)
    board[comp_choice] = user_type
    draw_board(board)

#Create a fuction to check the winning parameter
def check_win(board,x_o):
    if board[0] == x_o and board[1] == x_o and board[2] == x_o  or board[3] == x_o and board[4] == x_o and board[5] == x_o or board[6] == x_o and board[7] == x_o and board[8] == x_o or board[0] == x_o and board[3] == x_o and board[6] == x_o or board[1] == x_o and board[4] == x_o and board[5] == x_o or board[2] == x_o and board[5] == x_o and board[8] == x_o or board[0] == x_o and board[4] == x_o and board[8] == x_o or board[2] == x_o and board[4] == x_o and board[6] == x_o:
        print("Yaay.. {} won the game.".format(x_o))
        play = False

    else:
        play = True
    return play


draw_board(board)
play = True
comp_frnd = input("Select 'c' for Computer and 'f' for Friend") #Option for an opponent


while play == True:
    user_move(board, 'X')
    play = check_win(board, 'X')
    if play == False:
        continue
#Condition as per user choice to play against computer or another friend
    if comp_frnd == 'f':
        user_move(board, 'O')
        play = check_win(board, 'O')
    elif comp_frnd == 'c':
        comp_move(board, 'O')
        play = check_win(board, 'O')
