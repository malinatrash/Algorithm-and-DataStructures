from collections import deque


def get_knight_moves(x, y, n):
    knight_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]
    possible_moves = []
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            possible_moves.append((nx, ny))
    return possible_moves


def get_king_moves(x, y, n):
    king_moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    possible_moves = []
    for dx, dy in king_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            possible_moves.append((nx, ny))
    return possible_moves


def bfs(board, n, start_x, start_y, end_x, end_y):
    queue = deque([(start_x, start_y, 0, 'K')])  # (x, y, steps, figure)
    visited = set()

    while queue:
        x, y, steps, figure = queue.popleft()

        if (x, y) == (end_x, end_y):
            return steps

        if (x, y, figure) in visited:
            continue

        visited.add((x, y, figure))

        possible_moves = get_knight_moves(x, y, n) if figure == 'K' else get_king_moves(x, y, n)

        for nx, ny in possible_moves:
            next_figure = figure

            if board[nx][ny] == 'K':
                next_figure = 'K'
            elif board[nx][ny] == 'G':
                next_figure = 'G'

            queue.append((nx, ny, steps + 1, next_figure))

    return -1


n = int(input())
board = [input() for _ in range(n)]

start_x, start_y = None, None
end_x, end_y = None, None
for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            start_x, start_y = i, j
        elif board[i][j] == 'F':
            end_x, end_y = i, j

min_steps = bfs(board, n, start_x, start_y, end_x, end_y)

print(min_steps)
