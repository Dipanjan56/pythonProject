def create_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = int(input(f'input for matrix[{i}][{j}]: '))
            row.append(num)
        matrix.append(row)
    print(matrix)
    return matrix


"""for matrix sum, both of the matrix should be equal in rows and column length"""


def matrix_sum(A, B):
    matrix_sum = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            sum = A[i][j] + B[i][j]
            row.append(sum)
        matrix_sum.append(row)
    print(matrix_sum)
    return matrix_sum


"""for multiplication there are certain rules/constraints:
1. A m*n, B n*k -> i.e. number of columns in A should be equal to number of rows in B
2. [A * B]ij = sum[ A ik * B kj] = AB m*k
"""


def matrix_multiplication():
    # take a 3x3 matrix
    A = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    # take a 3x4 matrix
    B = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]

    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # iterating by row of A
    for i in range(len(A)):

        # iterating by column by B
        for j in range(len(B[0])):

            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    print(result)



if __name__ == '__main__':
    # m = int(input(f'number of rows: '))
    # n = int(input(f'number of columns: '))
    # create_matrix(m, n)

    A = [[1, 2, 3], [3, 4, 9]]
    B = [[7, 5, 8], [8, 2, 10]]
    matrix_sum(A, B)
    matrix_multiplication()
