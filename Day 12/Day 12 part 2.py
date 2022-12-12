from collections import deque

board = [list(x.replace('\n', '')) for x in open('input.txt', 'rt')]

def get_end():
    end_pos = []
    for r, row in enumerate(board):
        for c, column in enumerate(row):
            if column == 'E':
                board[r][c] = 'z'
                end_pos.append(r)
                end_pos.append(c)
    return end_pos

def get_start():
    start_pos = []
    for r, row in enumerate(board):
        for c, column in enumerate(row):
            if column == 'a' or column == 'S':
                if column == 'S':
                    board[r][c] = 'a'
                start_pos.append([r, c])
    return start_pos

start_pos = get_start()
end_pos = get_end()
for n in range(len(start_pos)):
    nodes = deque()
    nodes.append((0, start_pos[n][0], start_pos[n][1]))  # (distance,row,column)
    visited = {(start_pos[n][0], start_pos[n][1])}
    while len(nodes) != 0:
        d, r, c = nodes.popleft()
        for current_r, current_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if current_r < 0 or current_c < 0 or current_r >= len(board) or current_c >= len(board[0]):
                continue
            elif (current_r, current_c) in visited:
                continue
            elif ord(board[current_r][current_c]) - ord(board[r][c]) > 1:
                continue
            elif (current_r, current_c) == (end_pos[0], end_pos[1]):
                if n == 0:
                    distance = d + 1
                elif d + 1 < distance:
                    distance = d + 1
                break
            visited.add((current_r, current_c))
            nodes.append((d + 1, current_r, current_c))

print(distance)
