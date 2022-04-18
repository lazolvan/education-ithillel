def check_winner(map: list[str]) -> str:
	if (map[0][1] == map[1][1] == map[2][2]) \
			or (map[0][2] == map[1][1] == map[2][0]) \
			or (map[0][1] == map[1][1] == map[2][1]) \
			or (map[1][0] == map[1][1] == map[1][2]):
		return map[1][1]
	elif (map[0][0] == map[0][1] == map[0][2]) \
			or (map[0][0] == map[1][0] == map[2][0]):
		return map[0][0]
	elif (map[2][0] == map[2][1] == map[2][2]) \
			or (map[0][2] == map[1][2] == map[2][2]):
		return map[2][2]
	else:
		return "Draw"

if __name__ == '__main__':
	map = ["X.O",
		   "XX.",
		   "XOO"]

	print(check_winner(map))
