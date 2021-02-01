class Board:
	def __init__(self, name1, name2):
		self.player1 = name1
		self.player2 = name2
		self.board = [[{1: " "}, {2: " "}, {3: " "}],
					  [{4: " "}, {5: " "}, {6: " "}],
					  [{7: " "}, {8: " "}, {9: " "}]]

	def fill(self, key, symbol):
		self.key = key
		for row in self.board:
			for dictionary in row:
				for key, value in dictionary.items():
					if key == self.key and dictionary[key] == " ":
						dictionary[key] = symbol

	def print_board(self):
		n = 1
		for row in self.board:
			n1, n2, n3 = row[0], row[1], row[2]
			# print(" ", n1[n], " | ", n2[n+1], " | ", n3[n+2], " ")
			print("{} | {} | {}".format(n1[n], n2[n+1], n3[n+2]))
			n += 3

	def check_for_winner(self):
		winner = ""
		if (self.board[0][0][1] == self.board[0][1][2] == self.board[0][2][3] == "X") or (self.board[0][0][1] == self.board[0][1][2] == self.board[0][2][3] == "O") :
			winner = self.board[0][0][1]

		elif (self.board[1][0][4] == self.board[1][1][5] == self.board[1][2][6] == "X") or (self.board[1][0][4] == self.board[1][1][5] == self.board[1][2][6] == "O"):
			winner = self.board[1][0][4]

		elif (self.board[2][0][7] == self.board[2][1][8] == self.board[2][2][9] == "X") or (self.board[2][0][7] == self.board[2][1][8] == self.board[2][2][9] == "O") :
			winner = self.board[2][0][7]

		elif (self.board[0][0][1] == self.board[1][0][4] == self.board[2][0][7] == "X") or (self.board[0][0][1] == self.board[1][0][4] == self.board[2][0][7] == "O"):
			winner = self.board[0][0][1]

		elif (self.board[0][1][2] == self.board[1][1][5] == self.board[2][1][8] == "X") or (self.board[0][1][2] == self.board[1][1][5] == self.board[2][1][8] == "O"):
			winner = self.board[0][1][2]

		elif (self.board[0][2][3] == self.board[1][2][6] == self.board[2][2][9] == "X") or (self.board[0][2][3] == self.board[1][2][6] == self.board[2][2][9] == "O"):
			winner = self.board[0][2][3]

		elif (self.board[0][0][1] == self.board[1][1][5] == self.board[2][2][9] == "X")	or (self.board[0][0][1] == self.board[1][1][5] == self.board[2][2][9] == "O"):
			winner = self.board[0][0][1]

		elif (self.board[0][2][3] == self.board[1][1][5] == self.board[2][0][7] == "X") or (self.board[0][2][3] == self.board[1][1][5] == self.board[2][0][7] == "O"):
			winner = self.board[0][2][3]




		return winner
		
	def reset():
		for row in self.board:
			for dictionary in row:
				for key, value in dictionary.items():
					dictionary[key] = " "



class Player:
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol

	def ask_for_input(self):
		try:
			self.position = int(input("Enter the position you want to enter. (0-9): "))
		except ValueError:
			print("enter a valid position")
			self.ask_for_input()
		return self.position
