def set_zero(matrix):
    rows, cols = set(), set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0


if __name__ == '__main__':
    test_case_1 = [[1, 2, 0],
                   [0, 5, 6],
                   [7, 8, 9]]

    output_1 = [[0, 0, 0],
                [0, 0, 0],
                [0, 8, 0]]

    set_zero(test_case_1)
    assert test_case_1 == output_1
