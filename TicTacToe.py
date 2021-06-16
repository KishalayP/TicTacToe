import random
import os

def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        # Set the game up here
        #pass

        board=['#' for i in range(11)]
        #display_board(board)
        l=player_input()
        turn=choose_first()
        print(f'Player 1 is {l[0]} starts. ')
        print(f'Player 2 is {l[1]} starts. ')
        print("-----------------------------")
        print(f'Player {l[turn]} starts!!!')

        while full_board_check(board)== False:
            turn=(turn%2)
            print("---------------------")
            print(f"PLayer {(turn%2)+1}'s turn.")
            position=player_choice(board,l[turn])
            place_marker(board,l[turn],position)
            v=win_check(board,l[turn])
            display_board(board)
            #print(position,v,l[turn])

            if v == "win":
                print(f"Player {l[turn]} wins.")
                replay()
            if full_board_check(board)==True:
                print("Game Tied!!!")
                replay()
            turn+=1

        if replay()== False:
            print("Exiting.....")
            break
        else:
            continue

if __name__ == '__main__':
    main()



def display_board(board):
    clear()
    for i in range(7,0,-3):
        for j in range(2):
            print(f"{board[i+j]} | ",end="")
        print(f"{board[i+j+1]}",end="")
        print("")
        if i>1:
            print("---------")

def clear():
    os.system( 'cls' )

def player_input():
    player2=['X','O']
    while len(player2)==2:
        chk=str(input("Enter marker for Player 1: "))
        chk=chk.upper()
        if chk not in player2:
            continue
        player2.remove(chk)
    return [chk,player2[0]]


def place_marker(board, marker, position):
    board[position]=marker


def win_check(board, mark):
    for i in range(1,4):
        if board[i]==mark and board[i+3]==mark and board[i+6]==mark:
            return "win"
        elif i!=2 and board[i]==mark and board[i+1]==mark and board[i+2]==mark:
            return "win"
        elif i==1 and board[i]==mark and board[i+4]==mark and board[i+8]==mark:
            return "win"
        elif i==3 and board[i]==mark and board[i+2]==mark and board[i+4]==mark:
            return "win"
    for i in range(6,10,3):
        if board[i]==mark and board[i-1]==mark and board[i-2]==mark:
            return "win"
    return "loss"


def choose_first():
    return random.randint(0,1)


def space_check(board, position):
    if board[position]=='#':
        return True
    return False


def full_board_check(board):
    if  '#' not in board[1:]:
        return True 
    return False
    

def player_choice(board,mark):
    
    chk=False
    while chk == False:
        pos=int(input(f"Enter position to mark {mark}: "))
        chk=space_check(board,pos)   
        if chk== False:
            print(f"Space occupied, enter another position to mark {mark}")
    return pos


def replay():
    chk=input("Enter Y to play again or press N to quit. ")
    if chk.lower()=='y':
        return True
    return False


    