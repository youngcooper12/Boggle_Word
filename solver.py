def main():
    board = []
    for i in range(0,4):
        board.append([])
        for j in range(0,4):
            board[i].append(input().strip().upper())

    for i in range(0,4):
        for j in range(0,4):
            print(board[i][j], end = " ")
        print()
main()                    