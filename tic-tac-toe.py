board = [" "] * 9
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
def is_full():
    return " " not in board
def ai_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "
    if board[4] == " ":
        board[4] = "O"
        return
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return
print("TIC-TAC-TOE")
print("You = X")
print("AI  = O")
while True:
    print_board()
    position = int(input("Enter position (1-9): ")) - 1
    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move!")
        continue
    board[position] = "X"
    if check_winner("X"):
        print_board()
        print("You Win!")
        break
    if is_full():
        print_board()
        print("Draw!")
        break
    ai_move()
    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break
    if is_full():
        print_board()
        print("Draw!")
        break