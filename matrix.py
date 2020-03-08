rows=int(input())
cols=int(input())
matrix=[]
for i in range(0,rows):
        matrix.append(list(map(int,input().split(' ')[:cols])))
digits=[]
for r in range(0,rows):
    for c in range(0,cols):
        if(c<cols-3 and r<rows):
            if(matrix[r][c]==matrix[r][c+1]==matrix[r][c+2]==matrix[r][c+3]):
                digits.append(matrix[r][c])
                print(matrix[r][c],r,c,'row')
        if(c<cols and r<rows-3):
            if(matrix[r][c]==matrix[r+1][c]==matrix[r+2][c]==matrix[r+3][c]):
                digits.append(matrix[r][c])
                print(matrix[r][c],r,c,'col')
        if(c<cols+3 and r<rows-3):
            if(matrix[r][c]==matrix[r+1][c-1]==matrix[r+2][c-2]==matrix[r+3][c-3]):
                digits.append(matrix[r][c])
                print(matrix[r][c],r,c,'d1')
        if(c<cols-3 and r<rows-3):
            if(matrix[r][c]==matrix[r+1][c+1]==matrix[r+2][c+2]==matrix[r+3][c+3]):
                digits.append(matrix[r][c])
                print(matrix[r][c],r,c,'d2')
print(digits)
