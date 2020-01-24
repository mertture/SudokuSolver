template = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]]
#easy


# template = [[0, 0, 7, 8, 0, 0, 0, 0, 0],
#             [0, 0, 3, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 2, 0, 0, 0, 1, 6],
#             [6, 0, 0, 0, 0, 0, 0, 0, 2],
#             [0, 5, 0, 0, 0, 3, 0, 0, 0],
#             [0, 0, 0, 0, 0, 7, 8, 0, 4],
#             [2, 0, 0, 9, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 4, 7, 0]]
#medium

# template = [[0, 0, 5, 3, 0, 0, 0, 0, 0],
#             [8, 0, 0, 0, 0, 0, 0, 2, 0],
#             [0, 7, 0, 0, 1, 0, 5, 0, 0],
#             [4, 0, 0, 0, 0, 5, 3, 0, 0],
#             [0, 1, 0, 0, 7, 0, 0, 0, 6],
#             [0, 0, 3, 2, 0, 0, 0, 8, 0],
#             [0, 6, 0, 5, 0, 0, 0, 0, 9],
#             [0, 0, 4, 0, 0, 0, 0, 3, 0],
#             [0, 0, 0, 0, 0, 9, 7, 0, 0]]
#hard

def bigchecker(template, number, row, column):
  #Checking Columns
  
  for i in range(9):
    if template[i][column] == number and row != i:
      return False
  #Checking Rows
  
  for m in range(9):
    if template[row][m] == number and column != m:
      return False
# Checking Cubes
  rangr = row % 3
  rangc = column % 3
  for n in range((row-rangr), (row-rangr+3)):
    for t in range((column-rangc),(column-rangc+3)):     
      if template[n][t] == number and column != t and row != n:
        return False
  return True 



  
#Changes numbers

def solve(template):
   
  find = zeros()
  if not find:
    return True
  else:
    row, column = find
    
  
  for number in range(1,10):
    template[row][column] = number
    if bigchecker(template, number, row, column):
      template[row][column] == number
      if solve(template):
        return True
       
    template[row][column] = 0
      
  return False



  

#Where to change numbers
def zeros():
  for r in range(0,9):
    for c in range(0,9):
      if template[r][c] == 0:
        return(r, c)
  return None


#printing realistic
def print_sudoku(template):
  
  for i in range(9):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - -")
    
    for k in range(9):
      if k % 3 == 0 and k != 0:
        print(" | ", end ="")
      if k == 8:
        print(template[i][k])
      else:
        print(str(template[i][k]) + " ", end="")
    
solve(template)
print_sudoku(template)
