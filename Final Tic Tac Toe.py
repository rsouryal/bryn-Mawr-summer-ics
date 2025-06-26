
board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def print_board():
    for row in board:
        print(" ".join(row))
    print()

def check_winner(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_full():
    for row in board:
        for cell in row:
            if cell == ".":
                return False
    return True

def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

def play_game():
    # Clear the board at the start of each game
    for i in range(3):
        for j in range(3):
            board[i][j] = "."
    current_player = "X"
    while True:
        print_board()
        print("Player", current_player, "turn.")
        print("Type 'q' at any prompt to quit.")
        try:
            row_input = input("Enter row (0, 1, or 2): ")
            if row_input.lower() == "q":
                print("Game quit.")
                break
            row = int(row_input)
            col_input = input("Enter column (0, 1, or 2): ")
            if col_input.lower() == "q":
                print("Game quit.")
                break
            col = int(col_input)
        except ValueError:
            print("Please enter a number.")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row and column must be 0, 1, or 2.")
            continue
        if board[row][col] != ".":
            print("That spot is already taken!")
            continue
        board[row][col] = current_player
        if check_winner(current_player):
            print_board()
            print("Player", current_player, "wins!")
            break
        if is_full():
            print_board()
            print("It's a tie!")
            break
        current_player = switch_player(current_player)

# Run the

