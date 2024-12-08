def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player} ({'X' if player == 1 else 'O'}), enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == " ":
                board[row][col] = "X" if player == 1 else "O"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9s")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 1

    while True:
        display_board(board)
        get_player_move(board, current_player)
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {1 if winner == 'X' else 2} ({winner}) wins!")
            break
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = 3 - current_player

if __name__ == "__main__":
    play_game()
