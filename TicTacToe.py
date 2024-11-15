import random

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def get_player_move(board, player):
    while True:
        move = int(input(f"{player}'s turn. Enter your move (1-9): ")) - 1
        if board[move] == " ":
            return move
        print("That square is already taken. Try again.")

def get_computer_move(board):
    available_moves = [i for i, x in enumerate(board) if x == " "]
    return random.choice(available_moves)

def play_game():
    board = [" "] * 9
    player1_symbol = "X"
    player2_symbol = "O"

    game_mode = input("Select game mode (1 for single player, 2 for two players): ")
    if game_mode == "1":
        while True:
            print_board(board)
            player_move = get_player_move(board, player1_symbol)
            board[player_move] = player1_symbol
            if check_win(board, player1_symbol):
                print_board(board)
                print("You win!")
                return
            if " " not in board:
                print_board(board)
                print("It's a tie!")
                return

            computer_move = get_computer_move(board)
            board[computer_move] = player2_symbol
            if check_win(board, player2_symbol):
                print_board(board)
                print("Computer wins!")
                return
    else:
        while True:
            print_board(board)
            player1_move = get_player_move(board, player1_symbol)
            board[player1_move] = player1_symbol
            if check_win(board, player1_symbol):
                print_board(board)
                print("Player 1 wins!")
                return
            if " " not in board:
                print_board(board)
                print("It's a tie!")
                return

            player2_move = get_player_move(board, player2_symbol)
            board[player2_move] = player2_symbol
            if check_win(board, player2_symbol):
                print_board(board)
                print("Player 2 wins!")
                return

play_game()