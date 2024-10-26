from rocket import RocketBoard

board = RocketBoard(2)
# board2 = RocketBoard()
# print(board.rockets[1].altitude)
print(board[0])
board[0] = 50
print(board[0])

print(RocketBoard.get_distance(board[0],board[1]))
print(str(board[1]))