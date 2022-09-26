from utils import *

class MatrixCustom:
    def __init__(self, array):

        '''
        input: arr
            arr: array of matrix for each rows
        '''
        self.arr = array
        self.matrix = self.get_matrix()
    
    def get_matrix(self):
        '''
        func will return an matrix with array input
        '''
        matrix = [[0 for col in range(len(self.arr[0]))] for row in range(len(self.arr))]
        for row in range(len(self.arr)):
            for col in range(len(self.arr[0])):
                matrix[row][col] = self.arr[row][col]
        return matrix
    
    def shape_matrix(self):
        '''
            func for get shape matrix
        '''
        return (len(self.matrix), len(self.matrix[0]))
    
    def view_matrix(self):
        '''
            func for showing matrix
        '''
        print(self.matrix)
    
    @property
    def transpose(self):
        '''
            Transpose of matrix
        '''
        matrix_transpose = MatrixCustom(self.matrix)
        matrix_transpose.matrix = [[0 for row in range(len(self.matrix))] for col in range(len(self.matrix[0]))]
        
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                matrix_transpose.matrix[col][row] = self.matrix[row][col]
        return matrix_transpose

    '''
        basices operator for matrix
    '''

    def __add__(self, other_matrix):
        '''
            Add two matrices
        '''
        matrix_add = MatrixCustom(self.matrix)
        matrix_add.matrix = [[0 for col in range(len(self.matrix[0]))] for row in range(len(self.matrix))]
        for index_row in range(len(self.matrix)):
            for index_col in range(len(self.matrix[0])):
                matrix_add.matrix[index_row][index_col] = self.matrix[index_row][index_col] + other_matrix.matrix[index_row][index_col]
        return matrix_add
                

    def __sub__(self, other_matrix):
        '''
            Sub two matrices
        '''
        matrix_add = MatrixCustom(self.matrix)
        matrix_add.matrix = [[0 for col in range(len(self.matrix[0]))] for row in range(len(self.matrix))]
        for index_row in range(len(self.matrix)):
            for index_col in range(len(self.matrix[0])):
                matrix_add.matrix[index_row][index_col] = self.matrix[index_row][index_col] - other_matrix.matrix[index_row][index_col]
        return matrix_add

    def dot(self,vector_A, vector_B):
        return sum([a*b for a,b in zip(vector_A, vector_B)])

    def __mul__(self, other_matrix):
        
        '''
            this func is the dot product (or inner product) between 2 matrices
            NOTE: it's not element wise
        '''
        matrix_mul = MatrixCustom(self.matrix)
        matrix_mul.matrix = [[0 for row in range(len(self.matrix))] for row in range(len(self.matrix))]
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix)):
                matrix_mul.matrix[row][col] = self.dot(self.matrix[row], other_matrix.transpose.matrix[col])
        return matrix_mul

    def element_wise(self, other_matrix):
        '''
            func for product element-wise with 2 matrices
        '''
        matrix_add = MatrixCustom(self.matrix)
        matrix_add.matrix = [[0 for col in range(len(self.matrix[0]))] for row in range(len(self.matrix))]
        for index_row in range(len(self.matrix)):
            for index_col in range(len(self.matrix[0])):
                matrix_add.matrix[index_row][index_col] = self.matrix[index_row][index_col] * other_matrix.matrix[index_row][index_col]
        return matrix_add

    def matrix_inverse(self):
        pass
    
    def elimination(self):
        '''
            Return echelon form of matrix
        '''
        elimination_form_matrix = MatrixCustom(self.matrix)
        elimination_form_matrix.matrix = echelon_form(self.matrix)
        return elimination_form_matrix

    def rank(self):
        '''
            Return rank of matrix
        '''
        row_equal_zero = 0
        for rows in self.matrix:
            if all(row == 0 for row in rows):
                row_equal_zero += 1
        return len(self.matrix) - row_equal_zero


    def factorize_L_U(self):
        '''
            Return two matrices are L (Low) and U (Upp) for A = L.U
        '''
        u = MatrixCustom(self.matrix)
        l = MatrixCustom(self.matrix)
        u.matrix, ratio_column = echelon_form(self.matrix)
        l.matrix = [[1 if i == j else 0 for i in range(len(self.matrix))] for j in range(len(self.matrix))]
        for index_column, value_column in enumerate(ratio_column):
            for index_row, value_row in enumerate(value_column):
                l.matrix[len(self.matrix) - index_row - 1][index_column] = value_column[len(value_column) - index_row - 1][0]
        return l, u

    def permutation(self):
        pass

    def factorize_Q_R(self):
        pass
    



def main():
    matrix_A = MatrixCustom([[7,3,-1,2], [3,8,1,-4], [-1,1,4,-1], [2,-4,-1,6]])
    # matrix_B = MatrixCustom([[7, 3, -1, 2], [0.0, 6.714285714285714, 1.4285714285714286, -4.857142857142857], [0.0, 0.0, 3.5531914893617023, 0.3191489361702128], [0.0, 0.0, 0.0, 1.8862275449101804]])
    print(type(matrix_A))
    
    # matrix_A.view_matrix()
    # matrix_A.shape_matrix()

    # matrix_A.transpose
    
    # mul = matrix_A * matrix_B
    # mul.view_matrix()
    
    #add = matrix_A + matrix_B
    #add.view_matrix()

    #sub = matrix_A - matrix_B
    #sub.view_matrix()

    #matrix_elementwise = matrix_A.element_wise()

    # low,up = matrix_A.factorize_L_U()
    #low.view_matrix
    #upper.view_matrix

    # rankA = up.rank()
    # print(rankA)

if __name__ == "__main__":
    main()
