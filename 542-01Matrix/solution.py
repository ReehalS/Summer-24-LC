# 401ms (90.02%), 19.34MB (77.89%)

# bfs
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque() # double ended queue
        MAX= m*n

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j]=MAX
        
        while queue:
            row,col = queue.popleft()
            if(0<=row+1<m and 0<=col<n and mat[row+1][col]>mat[row][col]+1): # down
                queue.append((row+1, col))
                mat[row+1][col] = mat[row][col] +1
            if(0<=row-1<m and 0<=col<n and mat[row-1][col]>mat[row][col]+1): # top
                queue.append((row-1, col))
                mat[row-1][col] = mat[row][col] +1
            if(0<=row<m and 0<=col+1<n and mat[row][col+1]>mat[row][col]+1): # right
                queue.append((row, col+1))
                mat[row][col+1] = mat[row][col] +1
            if(0<=row<m and 0<=col-1<n and mat[row][col-1]>mat[row][col]+1): # left
                queue.append((row, col-1))
                mat[row][col-1] = mat[row][col] +1

        return mat
