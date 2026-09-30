import random
import os.path
import json
random.seed()

def draw_board(board):
    """Draw the Noughts and Crosses board."""
    for row in range(0, len(board)):
        print('\t ' + str('-' * (len(board) * 3 + len(board) - 1)))
        output = '\t'
        for col in range(0, len(board[row])):
            output += '| ' + board[row][col]
            if board[row][col].isdigit() < 10:
                output += ' '
            output += '|'
        print(output)
    print('\t ' + str('-' * (len(board) * 3 + len(board) - 1)))

def welcome(board):
    """Print the welcome message and display the board."""
    print("Welcome to the \"Unbeatable Noughts and Crosses\" game.")
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    """Set all elements of the board to one space ' '."""
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    print("The game begins")
    draw_board(board)
    return board

def get_player_move(board):
    """Ask the player for the cell to place their 'X'."""
    while True:
        try:
            move = int(input("Choose your square (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3  # Calculate row index
                col = (move - 1) % 3   # Calculate column index
                if board[row][col] == ' ':  # Check if the cell is empty
                    board[row][col] = 'X'  # Place the X in the chosen cell
                    return row, col  # Return the row and column indices
                else:
                    print("That square is already occupied. Please choose another.")
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    """Let the computer choose a cell to place a 'O'."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_for_win(board, 'O'):
                    return row, col  # Found a winning move
                board[row][col] = ' '  # Revert the board

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'  # Temporarily place X
                if check_for_win(board, 'X'):
                    board[row][col] = 'O'  # Block the player's win
                    return row, col
                board[row][col] = ' '  # Revert the board

    # Prioritize corners and center (general strategy)
    priority_moves = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
    random.shuffle(priority_moves)  # Randomize for variability
    for row, col in priority_moves:
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

    # Choose a random empty cell as a last resort
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

def check_for_win(board, mark):
    """Check if the player or computer has won."""
    for a in range(len(board)):
        if all(cell == mark for cell in board[a]) or all(board[b][a] == mark for b in range(len(board))):
            return True
    if all(board[i][i] == mark for i in range(len(board))) or all(board[i][len(board) - 1 - i] == mark for i in range(len(board))):
        return True
    return False

def check_for_draw(board):
    """Check if all cells are occupied."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game(board):
    """The game loop where the player and computer take turns."""
    initialise_board(board)
    draw_board(board)

    while True:
        # Player's move
        get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations! You won!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        # Computer's move
        choose_computer_move(board)
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    """Get user input for game options."""
    while True:
        print("Enter one of the following options:")
        print("\t1 - Play the game")
        print("\t2 - Save your score in the leaderboard")
        print("\t3 - Load and display the leaderboard")
        print("\tq - End the program")
        choice = input("1, 2, 3, or q? ")
        if choice in ['1', '2', '3', 'q']:
            return choice
        print("Invalid input. Please enter 1, 2, 3, or q.")

def load_scores():
    """Load the leaderboard scores from 'leaderboard.txt'."""
    leaders = {}
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                print("Error loading leaderboard. Creating a new one.")
    return leaders

def save_score(score):
    """Save the player's score to 'leaderboard.txt'."""
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)

def display_leaderboard(leaders):
    """Display the leaderboard scores."""
    print("\nLeaderboard:")
    if not leaders:
        print("No scores available.")
    else:
        print("{:<15} {:<10}".format("Name", "Score"))
        for name, score in sorted(leaders.items(), key=lambda x: x[1], reverse=True):
            print("{:<15} {:<10}".format(name, score))