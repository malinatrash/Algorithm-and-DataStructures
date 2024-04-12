def print_operations(operations):
    print(len(operations))
    for op in operations:
        print(*op)


def rotate_clockwise(matrix):
    operations = []
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Обмен между 4 ячейками
            top_left = (i, j)
            top_right = (j, n - i - 1)
            bottom_right = (n - i - 1, n - j - 1)
            bottom_left = (n - j - 1, i)

            operations.append((top_left, top_right))
            operations.append((top_left, bottom_left))
            operations.append((bottom_left, bottom_right))
            operations.append((top_right, bottom_right))

            # Обмен значений
            matrix[top_left[0]][top_left[1]], matrix[top_right[0]][top_right[1]] = matrix[top_right[0]][top_right[1]], \
            matrix[top_left[0]][top_left[1]]
            matrix[top_left[0]][top_left[1]], matrix[bottom_left[0]][bottom_left[1]] = matrix[bottom_left[0]][
                bottom_left[1]], matrix[top_left[0]][top_left[1]]
            matrix[bottom_left[0]][bottom_left[1]], matrix[bottom_right[0]][bottom_right[1]] = matrix[bottom_right[0]][
                bottom_right[1]], matrix[bottom_left[0]][bottom_left[1]]

    print_operations(operations)


def rotate_counter_clockwise(matrix):
    operations = []
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Обмен между 4 ячейками
            top_left = (i, j)
            top_right = (j, n - i - 1)
            bottom_right = (n - i - 1, n - j - 1)
            bottom_left = (n - j - 1, i)

            operations.append((top_left, bottom_left))
            operations.append((top_left, top_right))
            operations.append((bottom_left, bottom_right))
            operations.append((top_right, bottom_right))

            # Обмен значений
            matrix[top_left[0]][top_left[1]], matrix[bottom_left[0]][bottom_left[1]] = matrix[bottom_left[0]][
                bottom_left[1]], matrix[top_left[0]][top_left[1]]
            matrix[top_left[0]][top_left[1]], matrix[top_right[0]][top_right[1]] = matrix[top_right[0]][top_right[1]], \
            matrix[top_left[0]][top_left[1]]
            matrix[bottom_left[0]][bottom_left[1]], matrix[bottom_right[0]][bottom_right[1]] = matrix[bottom_right[0]][
                bottom_right[1]], matrix[bottom_left[0]][bottom_left[1]]

    print_operations(operations)


# Считываем входные данные
n, direction = input().split()
n = int(n)
matrix = [list(map(int, input().split())) for _ in range(n)]

# Выполняем поворот матрицы в зависимости от указанного направления
if direction == 'R':
    rotate_clockwise(matrix)
else:
    rotate_counter_clockwise(matrix)
