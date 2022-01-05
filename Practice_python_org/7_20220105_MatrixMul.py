A = [[1, 2],
    [3,4]]

B = [[1, 2, 3, 4 ,5],
     [5 ,6 ,7 ,8 ,9]]

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