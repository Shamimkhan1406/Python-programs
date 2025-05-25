import math

# Display the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print("-" * 5)

# Check for win conditions
def check_winner(board, player):
    # Rows, columns, and diagonals
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2 - i] for i in range(3)].count(player) == 3:
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm to determine the best move for the AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Determine the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game function
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the AI is O.")
    print_board(board)
    
    while True:
        # Player move
        player_row = int(input("Enter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))
        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'X'
            print_board(board)
            if check_winner(board, 'X'):
                print("Congratulations! You win!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
        else:
            print("Cell already taken. Try again.")
            continue

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
            print("AI's Move:")
            print_board(board)
            if check_winner(board, 'O'):
                print("AI wins! Better luck next time.")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
