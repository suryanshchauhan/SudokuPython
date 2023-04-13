def SudokuSolver():
    # Prompt user to enter the file name
    file_name = input("Please enter the file name: ")
    sudoku = []
    
    # Open the file and read the puzzle
    with open(file_name, "r") as fileHandle:
        puzzle = fileHandle.readlines()
    
    # Process the puzzle and create the sudoku
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line] = puzzle[line][:-1]
        
        sudoku.append(list(map(int, puzzle[line].split(" "))))
    
    return sudoku

def findEmpty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def valid(sudoku, num, pos):
    row = pos[0]
    column = pos[1]

    # Check row
    for i in range(len(sudoku[0])):
        if sudoku[row][i] == num and column != i:
            return False

    # Check column
    for i in range(len(sudoku)):
        if sudoku[i][column] == num and row != i:
            return False

    # Check box
    startRowBox = row // 3
    startColumnBox = column // 3
    for i in range(startRowBox * 3, (startRowBox * 3) + 3):
        for j in range(startColumnBox * 3, (startColumnBox * 3) + 3):
            if sudoku[i][j] == num and row != i and column != j:
                return False
                
    return True

def printSudoku(sudoku):
    if not findEmpty(sudoku):
        print("Finished Sudoku")
    else:
        print("Unsolved Sudoku")
    
    for i in range(len(sudoku)):
        if i % 3 == 0:
            print("-------------------")
        
        for j in range(len(sudoku[0])):
            if j % 3 == 0:
                print("\b|", end="")
            
            print(str(sudoku[i][j]) + " ", end="")
        print("\b|")
    print("-------------------")

def solve(sudoku):
    find = findEmpty(sudoku)
    
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(sudoku, i, find):
            sudoku[row][col] = i
            
            if solve(sudoku):
                return True
            
            sudoku[row][col] = 0
    
    return False

sudoku = SudokuSolver()
printSudoku(sudoku)
solve(sudoku)
printSudoku(sudoku)
