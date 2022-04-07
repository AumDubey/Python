board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def solve(b):
    
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(b, i, (row, col)):
            b[row][col] = i
            
            if solve(b):
                return True
            
            b[row][col] = 0
            
    return False
    

def valid(b, num, pos):
    # check row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(b[0])):
        if b[i][pos[1]] == num and pos[1] != i:
            return False
    # check box
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    
    for i in range(square_y * 3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False
                
    return True

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return(i,j)
    return None


print_board(board)
solve(board)
print("_________________________")
print(" ")
print_board(board)
