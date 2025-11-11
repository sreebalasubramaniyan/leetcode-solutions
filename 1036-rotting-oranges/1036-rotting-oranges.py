class Solution(object):
    def orangesRotting(self, grid):
        """
        
        """
        arr = [1,2,3]
        temp = arr[:]
        temp[1] = 1
        print(arr)
        # find the no of fresh oranges
        M = len(grid)
        N = len(grid[0]) 
        fresh = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0 : return 0
        minutes = 0
        prev = fresh 
        while True:
            temp = copy.deepcopy(grid)
            isFresh = True
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1:
                        for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                            if 0<=r<M and 0<=c<N and grid[r][c]==2:
                                temp[i][j] = 2
                                fresh -= 1
                                isFresh = False
                                break
            minutes += 1
            if fresh == 0 or isFresh:
                break
            grid = temp

        return minutes if not fresh else -1
            
            
    