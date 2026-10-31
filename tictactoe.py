import random
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
        
    return None

while True:
    display()

    pos=int(input("Enter position (1-9)")) - 1
    if pos < 0 or pos>8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue
    board[pos] = "x"
    
    if check_winner()=="x":
        display()
        print("you win")
        break
    if " " not in board:
        display()
        print("draw")
        break

    pos=random.choice([i for i in range(9) if board[i]==" "])
    board[pos]="0"

    print("computer selected position:", pos+1)

    if check_winner()=="0":
        display()
        print("computer wins")
        break
    if " " not in board:
        display()
        print("its a draw")
        break