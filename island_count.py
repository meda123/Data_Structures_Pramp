
#Island Count# 

""" 
    Given a 2D array binaryMatrix of 0s and 1s, implement a function 
    getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

    An island is defined as a group of adjacent values that are all 1s. A cell 
    in binaryMatrix is considered adjacent to another cell if they are next to each 
    either on the same row or column. Note that two values of 1 are not part of the
    same island if they’re sharing only a mutual corner (i.e. they are diagonally 
    neighbors).

    Explain and code the most efficient solution possible and analyze its time and 
    space complexities

    Example: 
    input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                             [0,    0,    1,    1,    1],
                             [1,    0,    0,    1,    0],
                             [0,    1,    1,    0,    0],
                             [1,    0,    1,    0,    1] ]
    output: 6 # since this is the number of islands in binaryMatrix.
              # See all 6 islands color-coded below.


"""


binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]

def num_islands(m):

    visited = set()

    islands = 0

    for i in range(5):

        for j in range(5):

            if m[i][j] == 1:

                visited.add((i,j))

                if i == 0 and j == 0:

                    islands += 1

                elif i == 0:

                    if m[i][j-1] == 1:

                        continue # we have visited this island

                    else:

                        islands += 1

                else:

                    if (i-1,j-1) in visited or (i-1,j+1) in visited or (i-1,j) in visited or (i,j-1) in visited:
                        continue

                    else:

                        islands += 1

    # print visited

    return islands

print num_islands(binaryMatrix)



############## Problem below is a varation and it works  ######################


# Program to count islands in boolean 2D matrix
class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    # A function to check if a given cell 
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1 
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
             
 
    # A utility function to do DFS for a 2D 
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):
 
        # These arrays are used to get row and 
        # column numbers of 8 neighbours 
        # of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
         
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)
 
 
    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
 
        # Initialize count as 0 and travese 
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, 
                # then new island found
                if visited[i][j] == False and self.graph[i][j] ==1:
                    # Visit all cells in this island 
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1
 
        return count
 
graph = [[0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g= Graph(row, col, graph)
 
print "Number of islands is :"
print g.countIslands()