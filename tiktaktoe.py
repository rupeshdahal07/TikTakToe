# Initialize the game board
board = [" " for _ in range(9)]

def display_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def player_input(player_symbol):
    while True :
        try:
            move = int(input(f"Player {player_symbol}, enter your move (1-9): "))
            if move<0 or move>9 or board[move] != " ":
                print('Invalid number. Try again')
            
            else:
                board[move] = player_symbol
                break
                
        except ValueError:
            print('Please enter a vaid number.')
            
            
            
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None


def main():
    print("Welcome to Tic-Tac-Toe!")
    display_board()
    
    current_player = "X"
    while True:
        player_input(current_player)
        display_board()
        
        winner = check_winner()
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()

    
            
                
    
