Data = open('input.txt','rt')
Data = [x.replace('\n','') for x in Data]
Data = [x.split(' ') for x in Data]
print(Data)
board = []

def format_board_size():
    Max = 0
    for y in Data:
        if int(y[1]) > Max:
            Max = int(y[1])
    for x in range(Max):
        row = []
        for y in range(Max):
            row.append('.')
        board.append(row)

def print_board(Board_input):
    for row in Board_input:
        print(row)


format_board_size()
board[-1][0] = 'H'
board_t = board.copy()
board_t[-1][0] = 'T'
print_board(board_t)
print_board(board)