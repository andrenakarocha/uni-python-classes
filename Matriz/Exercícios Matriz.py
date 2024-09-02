from matplotlib import pyplot as plt


def print_matrix(matrix):
    output = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output += f"{matrix[i][j]}  "
        output += "\n"
    print(output)
    return


def generate_matrix(lines, collums):
    matriz = []
    for i in range(lines):
        matriz.append([])
        for j in range(collums):
            matriz[i].append(0)
    return matriz


def diagonal_change(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
    print_matrix(matrix)
    return


def counter_diagonal_change(matrix):
    for i in range(len(matrix)):
        matrix[i][len(matrix) - 1 + i] = 1
    print_matrix(matrix)
    return


def reverse_diagonal_change(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not i == j and not j == ((len(matrix) - 1) - i):
                matrix[i][j] = 1
    print_matrix(matrix)
    return


def transpost_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            aux = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = aux
    print_matrix(matrix)
    return

def calculate_grades(grades):
    weight = [1, 2, 3, 2, 1]
    medias = [0] * len(grades[0])
    for i in range(len(grades[0])):
        for j in range(len(grades)):
            grades[j][i] *= weight[j]
            medias[i] += grades[j][i]
        weight_sum = 0
        for w in weight:
            weight_sum += w
        medias[i] /= weight_sum

    print(medias)
    return medias

def show_chess_board(lines, collums):
    matrix = []
    for i in range(lines):
        matrix.append([])
        for j in range(collums):
            if (i + j) % 2 == 0:
                matrix[i].append(0)
            else:
                matrix[i].append(1)
    plt.imshow(matrix, 'hot')
    plt.show()
    return

# print_matrix(generate_matrix(5, 5))
# Exercício 1

# generate_matrix(5, 5)
# Exercício 2

# diagonal_change(generate_matrix(5, 5))
# Exercício 3

# counter_diagonal_change(generate_matrix(5, 5))
# Exercício 4

# reverse_diagonal_change(generate_matrix(5, 5))
# Exercício 5

# transpost_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Exercício 6

calculate_grades([
    [10, 3, 10],
    [9, 7, 3],
    [5, 9, 6],
    [2, 1, 4],
    [8, 10, 9]
])

# show_chess_board(8, 8)
# Exercício 8
