def print_sol(board,n):
    for row in range(n):
        line = " "
        for col in range(n):
            if board[row] == col:
                line += "Q"
            else:
                line+= "."
        print(line)
    print()

def is_safe(board,row,col):
    for i in range(row):
        if board[i] == col:
            return False
        if  abs(board[i]-col) == abs(i - row):
            return False
    return True

def solve(board,row,n,solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    for col in range(n):
        if is_safe(board,row,col):
            board[row] = col 
            solve(board,row+1,n,solutions)
            board[row] = -1

def queen(n):
    board = [-1]*n 
    solutions = []
    solve(board,0,n,solutions)
    return solutions

n=int(input("Enter the no of queens:"))

res = queen(n)

for i, sol in enumerate(res,start=1):
    print(f"Solution for {i}")
    print_sol(sol,n)
