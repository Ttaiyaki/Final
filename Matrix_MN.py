'''Matrix_MN'''
def matrix(row, column):
    '''Matrix_MN'''
    matrix_list = []
    for _ in range(row):
        num_in_row = []
        for _ in range(column):
            num_in_row.append(int(input()))
        matrix_list.append(num_in_row)

    for i in range(row):
        for j in range(column):
            print(matrix_list[i][j], end=' ')
        print()
matrix(int(input()), int(input()))
