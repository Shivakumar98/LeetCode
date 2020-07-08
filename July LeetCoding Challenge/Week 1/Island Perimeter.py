You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        g=grid
        p=0
        
        # we will have parameter 4 if 1 is surrounded by 0
        # If 1 is surrounded by 1 then we subtract 2
        for i in range(m):
            for j in range(n):
                if g[i][j]==1:
                    p+=4
                    if i>0 and g[i-1][j]==1:
                        p-=2
                    if j>0 and g[i][j-1]==1:
                        p-=2
        return p
    
        
        # My Solution which did not work
#         m,n=len(grid),len(grid[0])
#         print(m,n)
#         g=grid
#         c=0
#         for i in range(m):
#             for j in range(n):
#                 if (i==0 or i==m-1) and g[i][j]==1:
#                     c+=1
#                 else:
#                     if (g[i-1][j]==0 and g[i][j]==1):
#                         c+=1
#                     if (g[i-1][j]==1 and g[i][j]==0) :
#                         c+=1
#                 if (j==0 or j==m-1) and g[i][j]==1:
#                     c+=1
#                 else:
#                     if (g[i][j-1]==0 and g[i][j-1]==1):
#                         c+=1
#                     if (g[i][j-1]==1 and g[i][j-1]==0):
#                         c+=1
                
                    
#         print(c)
                    
        
