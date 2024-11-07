def display_board(board):
    for row in board:
        print(" | ".join(row))
    print()


def check_winner(board, player) -> bool:
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(row[i] == player for row in board):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def game_over(board):
    return check_winner(board, "X") or check_winner(board, "O") or board_full(board)


def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


def minimax(board, depth, is_computer_turn):
    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif board_full(board):
        return 0

    if is_computer_turn:
        best_score = float("-inf")
        for row, col in available_moves(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in available_moves(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            best_score = min(best_score, score)
        return best_score


def get_best_move(board):
    best_score = float("-inf")
    best_move = None

    for row, col in available_moves(board):
        board[row][col] = "O"
        move_score = minimax(board, 0, False)
        board[row][col] = " "
        if move_score > best_score:
            best_score = move_score
            best_move = (row, col)

    return best_move


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while not game_over(board):
        display_board(board)
        
        # Player's move
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
            board[row][col] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if game_over(board):
            break

        # Computer's move
        print("Computer's move:")
        computer_move = get_best_move(board)
        board[computer_move[0]][computer_move[1]] = "O"

    display_board(board)
    if check_winner(board, "X"):
        print("You win!")
    elif check_winner(board, "O"):
        print("Computer wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_tic_tac_toe()
