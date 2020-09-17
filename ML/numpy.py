import numpy as np
def average(a,n):
    sum = np.cumsum(a,dtype=float)
    sum[n:]=sum[n:] - sum[:-n]
    return sum[n-1:]/n

a = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print(average(a, 3))


def matrix(ipvector, n, increasing=False):
    if not increasing:
        op_matx = np.array([x ** (n - 1 - i) for x in ipvector for i in range(n)]).reshape(ipvector.size, n)
    elif increasing:
        op_matx = np.array([x ** i for x in ipvector for i in range(n)]).reshape(ipvector.size, n)
    return op_matx

inputvector = np.array([1,2,3,4,5])
no_col_opmat = 3
op_matx_dec_order = matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = matrix(inputvector,no_col_opmat,True)


print("array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("array in increasing order of powers:\n\n",op_matx_inc_order,"\n")
