import matplotlib.pyplot as plt


def return_matrix_string(matrix):
    output = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output += f"{matrix[i][j]}  "
        output += "\n"
    return output


def generate_matrix(lines, collums):
    matriz = []
    for i in range(lines):
        matriz.append([])
        for j in range(collums):
            matriz[i].append(i)
    return matriz


def show_matrix_colors(matrix, color_map):
    plt.imshow(matrix, color_map)
    plt.colorbar()
    plt.show()


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


# return_matrix_string([[1, 2, 3], [4, 5, 6]])
# Retorna uma string formatada da matriz

# generate_matrix(10, 20)
# Uma função que cria matrizes com as linhas e colunas passadas como parâmetros

# show_matrix_colors(generate_matrix(20, 20), 'hot')
# Mostra a matriz de cores usando a lib matplotlib

show_chess_board(8, 8)
# Mostra uma matriz como um tabuleiro de xadrez
