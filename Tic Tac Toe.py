import random

def display_board(board):
	print("\n"*50)                                                                  # clears output
	print(board[7]+"|"+board[8]+"|"+board[9])
	print(board[4]+"|"+board[5]+"|"+board[6])
	print(board[1]+"|"+board[2]+"|"+board[3])

def player_input():      
	marker = ''
	while marker not in ["X","O","x","o"]:
		marker = input("Player 1 chooses 'X' or 'O': ").upper()

	if marker == "X":
		return ('X','O')
	else:
		return ('O','X')

def space_check(board, position):
	return board[position] == ' '

def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):  # checks for empty space
		position = int(input("Choose the position(1-9): "))
	return position

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board,mark):  
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def choose_first():                                             # To choose player randomly
	if random.randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True

def replay():
	x = input("Do you want to play again, Enter 'Y' or 'N': ")
	if x[0] == 'Y' or x[0] == 'y':
		return True
	else:
		return False

# Main code:

print("Welcome to Tic Tac Toe")

while True:

	board = [" "] * 10                                          # create an empty board                     
	player1, player2 = player_input()
	turn = choose_first()
	print(turn + " will go first.")
	game_on = True

	while game_on:                                              
		if turn == 'Player 1':
			display_board(board)
			position = player_choice(board)
			place_marker(board, player1, position)

			if win_check(board, player1):
				display_board(board)
				print("PLAYER 1 Wins!")
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print("Draw!!")
					game_on = False
				else:
					turn = 'Player 2'
		else:
			display_board(board)
			position = player_choice(board)
			place_marker(board, player2, position)

			if win_check(board, player2):
				display_board(board)
				print("PLAYER 2 Wins!")
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print("Draw!!")
					game_on = False
				else:
					turn = 'Player 1'
	if not replay():
		break
