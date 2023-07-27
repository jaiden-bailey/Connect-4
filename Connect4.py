#Jaiden Bailey


import random

#Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 21)
#Function to check if player has 4 in a row whether its in vertical, horizontal, or diagonal.
def check_win(board, player):
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

            if board[row][col+3] == player and board[row+1][col+2] == player and board[row+2][col+1] == player and board[row+3][col] == player:
                return True

    return False

def is_valid_move(board, col):
    return any(row[col] == " " for row in board)

def drop_piece(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return
#Function utilizes the random library to simulate a computer move.
def computer_move(board):
    valid_moves = [col for col in range(7) if is_valid_move(board, col)]
    return random.choice(valid_moves)

def play_connect_4():
    board = [[" " for _ in range(7)] for _ in range(6)]

    player1 = "X"
    player2 = "O"

    print_board(board)

    while True:
        # Moves for player 1 move
        col = int(input(f"Player 1 ({player1}), enter column (0-6): "))
        while not is_valid_move(board, col):
            col = int(input("Invalid move. Enter column (0-6): "))
        drop_piece(board, col, player1)
        print_board(board)
        if check_win(board, player1):
            print("Player 1 wins!")
            break

        # Checking for a tie
        if all(board[0][i] != " " for i in range(7)):
            print("It's a tie!")
            break

        # Moves for player 2 
        choice = input("Enter '1' to play against another player, or '2' to play against the computer: ")
        if choice == "1":
            col = int(input(f"Player 2 ({player2}), enter column (0-6): "))
            while not is_valid_move(board, col):
                col = int(input("Invalid move. Enter column (0-6): "))
        elif choice == "2":
            col = computer_move(board)
        else:
            print("Invalid choice. Exiting the game.")
            break

        drop_piece(board, col, player2)
        print_board(board)
        if check_win(board, player2):
            if choice == "2":
                print("Computer wins!")
            else:
                print("Player 2 wins!")
            break

if __name__ == "__main__":
    play_connect_4()

