from re import M
import sys

def escape_matrix(p, n, m, a, b):

    ret = [-1 for _ in range(0,m)]
    
    def MatrixFun(i, j, row = a, col = b, pap = p):
        return (a[i]*b[j])%pap

    def minPathFun(MatrixFun):
        temp = [[0 for i in range(m)] for i in range(2)]

        for i in range(1, m):
            temp[0][i] = temp[0][i-1] + MatrixFun(0, i)*2
        
        temp[1][0] = temp[0][0] + MatrixFun(1, 0)


        for i in range(1, n):
            for j in range(1, m):
                if temp[1][j-1] + 2 * MatrixFun(i, j) <= temp[0][j] + MatrixFun(i, j):
                    temp[1][j] = temp[1][j-1] + 2 * MatrixFun(i, j)
                else:
                    temp[1][j] = temp[0][j] + MatrixFun(i, j)
            temp[0] = temp[1]
            if i < n - 1:
                temp[1][0] = temp[0][0] + MatrixFun(i+1, 0)
        
        return temp[-1]
       
    ret = minPathFun(MatrixFun)

    return ret
SUBMIT_TO_SZKOPUL = True
#SUBMIT_TO_SZKOPUL = False

if SUBMIT_TO_SZKOPUL:
    reader = sys.stdin
else:
    reader = inputReader = open("input0b.txt","r")
 
# Reads the input
astr = reader.readline().split()
p=int(astr[0])
n=int(astr[1])
m=int(astr[2])
a = [int(val) for val in reader.readline().split()]
b = [int(val) for val in reader.readline().split()]

# Calls your function
ret = escape_matrix(p, n, m, a, b)

# Writes the output
for i in range(0,m):
    print(ret[i])
