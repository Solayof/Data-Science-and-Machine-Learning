import random

# Define the game board
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3])) # print each row
        if i < 2:
            print("---------")
    print("\n")

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player: # check if all positions are the same for the player
            return True
    return False

def check_tie():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if check_tie():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False) # switch to minimizing player
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True) # switch to maximizing player
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def main():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move, try again.")
            continue
        board[move] = "X"
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        if check_tie():
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if check_tie():
            print("It's a tie!")
            break

# Call the main loop
if __name__ == "__main__":
    main()
