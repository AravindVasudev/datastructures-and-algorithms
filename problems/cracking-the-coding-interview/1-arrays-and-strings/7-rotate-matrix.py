def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()


if __name__ == '__main__':
    test_case_1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    test_case_1_output = [[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]]

    rotate_matrix(test_case_1)
    assert test_case_1 == test_case_1_output
