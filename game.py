from classes import Board, Player

game_over = False
current_turn = 1

def start_game(board, player1, player2):
	global game_over, current_turn

	while not game_over:
		if current_turn == 1:
			position = player1.ask_for_input()
			board.fill(position, player1.symbol)
			current_turn = 2

		elif current_turn == 2:
			position = player2.ask_for_input()
			board.fill(position, player2.symbol)
			current_turn = 1


		board.print_board()
		winner = board.check_for_winner()
		if winner != "":
			if winner == "X":
				print("The winner is {}".format(player1.name))
			elif winner == "O":
				print("The winner is {}".format(player2.name))
			break

def ask_for_names():
	name1 = str(input("Enter the name of the first player.(X): "))
	name2 = str(input("Enter the name of the second player.(O): "))

	return [name1, name2]


if __name__ == "__main__":
	names = ask_for_names()

	player1 = Player(names[0], "X")
	player2 = Player(names[1], "O")
	board = Board(player1.name, player2.name)
	start_game(board, player1, player2)