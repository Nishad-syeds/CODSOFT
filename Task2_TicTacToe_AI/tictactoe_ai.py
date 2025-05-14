import math

def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[r][c] == player for r in range(3)) for c in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def board_is_full(board):
    return all(cell != " " for row in board for cell in row)

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax_algorithm(board, maximizing_player):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif board_is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for (r, c) in available_moves(board):
            board[r][c] = "O"
            eval = minimax_algorithm(board, False)
            board[r][c] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for (r, c) in available_moves(board):
            board[r][c] = "X"
            eval = minimax_algorithm(board, True)
            board[r][c] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def ai_turn(board):
    best_score = -math.inf
    best_move = None
    for (r, c) in available_moves(board):
        board[r][c] = "O"
        score = minimax_algorithm(board, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def start_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("🎮 Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O.")
    player_starts = input("Do you want to go first? (y/n): ").strip().lower() == 'y'

    while True:
        display_board(board)

        if player_starts:
            try:
                row, col = map(int, input("Enter your move (row and column: 0 1): ").split())
                if board[row][col] != " ":
                    print("Cell already taken. Try again.")
                    continue
                board[row][col] = "X"
                if check_winner(board, "X"):
                    display_board(board)
                    print("🎉 You win!")
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers (0, 1, or 2).")
                continue
        else:
            print("AI is making a move...")
            r, c = ai_turn(board)
            board[r][c] = "O"
            if check_winner(board, "O"):
                display_board(board)
                print("🤖 AI wins! You lose.")
                break

        if board_is_full(board):
            display_board(board)
            print("😐 It's a draw!")
            break

        player_starts = not player_starts

if __name__ == "__main__":
    start_game()
