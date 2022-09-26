def remove_element(vector_above, vector_below, index_pivot):
    '''
        get result by subtracted row above from row bellow
        input: vector_above, vector_below, index_pivot
            vector_above: row above
            vector_below: row bellow
            index_pivot: index of pivot
    '''

    while vector_above[index_pivot] == 0:
        index_pivot += 1
    ratio = vector_below[index_pivot]/vector_above[index_pivot]
    row_for_elimination = [ratio * i for i in vector_above]
    row_eliminated = [before_i - i for i, before_i in zip(row_for_elimination, vector_below)]
    return row_eliminated, ratio, index_pivot

def elimination(arr, pivots):
    '''
        Do elimination with ones row as pivot and rest of other row
    '''
    elimination_matrix = []
    matrix_ratio_col = []
    for i in range(pivots,len(arr)):
        if i == pivots:
            continue
        element , ratio, col_pivot = remove_element(arr[pivots], arr[i], pivots)
        elimination_matrix.append(element)
        matrix_ratio_col. append([ratio, col_pivot])
    return elimination_matrix, matrix_ratio_col
            


def echelon_form(arr):
    '''
        return elchelon form of matrix
        arr: array with 2-dimension
    '''
    echelon_form_matrix, ratio_col = elimination(arr,0)
    echelon_form_matrix.insert(0,arr[0])
    matrix_ratio_col = []
    matrix_ratio_col.append(ratio_col)
    for row_index in range(1,len(arr) - 1):
        tmp_echelon = echelon_form_matrix
        echelon_form_matrix, ratio_col = elimination(echelon_form_matrix, row_index)
        matrix_ratio_col.append(ratio_col)
        for i in range(row_index, -1, -1):
            echelon_form_matrix.insert(0, tmp_echelon[i])
    return echelon_form_matrix, matrix_ratio_col