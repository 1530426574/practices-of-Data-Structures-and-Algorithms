matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
l1 = len(matrix)
l2 = len(matrix[0])
a = [0] * l1 * l2
print(a)

for i in range(l1*l2):
    row, col = i//l2, i%l2
    c = matrix[row][col]
    print('row={},col={},c = {}'.format(row,col,c))
    a[i] =c
print(a)


#二维 -> 一维
def two_to_one(i,j,cols=3):
    return i*cols +j

#一维 -> 二维
def one_to_two(index,cols=3):
    return index//cols,index%cols

