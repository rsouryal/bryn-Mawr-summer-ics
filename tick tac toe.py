def right_diagonal_win(board):
    return board[0][2] == board[0][2] == board[1][1] == board[2][0]

board = [
    ['O', '0', 'X'],
    ['', 'X', 'O'],
    ['X', '0', '0']
]
print(right_diagonal_win(board))
