A  = [[1, 3, 4],
     [2 ,5 ,7],
     [5 ,9 ,6]]

B  = [[1, 0 ,0],
     [0 ,1 ,0],
     [0 ,0 ,1]]


def matrix_mul(A, B):
    if len(A[0])==len(B):
        final_mat = []
        for r in range(len(A[0])):
            C = [] 
            for c in range(len(B[0])):
                sum_mat = 0
                for k in range(len(A[0])):
                    sum_mat += A[r][k]*B[k][c]
                C.append(sum_mat)
            final_mat.append(C)
        print(final_mat)
    else:
        print("Matrix multiplication not possible")
    
    
matrix_mul(A, B)