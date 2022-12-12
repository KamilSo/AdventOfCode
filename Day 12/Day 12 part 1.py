from collections import deque

board = [list(x.replace('\n', '')) for x in open('input.txt', 'rt')]

def get_start_and_end():
    for r, row in enumerate(board):
        for c, column in enumerate(row):
            if column == 'S':
                start_row = r
                start_column = c
                board[r][c] = 'a'
            elif column == 'E':
                end_row = r
                end_column = c
                board[r][c] = 'z'
    return start_row, start_column, end_row, end_column

start_r, start_c, end_r, end_c = get_start_and_end()
nodes = deque()
nodes.append((0, start_r, start_c))  # (distance,row,column)
visited = {(start_r, start_c)}

while len(nodes) != 0:
    d, r, c = nodes.popleft()
    for current_r, current_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if current_r < 0 or current_c < 0 or current_r >= len(board) or current_c >= len(board[0]):
            continue
        if (current_r, current_c) in visited:
            continue
        if ord(board[current_r][current_c]) - ord(board[r][c]) > 1:
            continue
        if (current_r, current_c) == (end_r, end_c):
            print(d+1)
            nodes = []
            break
        visited.add((current_r, current_c))
        nodes.append((d + 1, current_r, current_c))
