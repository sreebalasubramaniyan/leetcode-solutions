class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        atlantic = set()
        pasific = set()

        def f(i,j,seen,prev):
            if(
                (i,j) in seen or i<0 or j<0 or i>=R or j>=C 
                or heights[i][j] < prev
            ):
                return
            seen.add((i,j))
            f(i+1,j,seen,heights[i][j])
            f(i-1,j,seen,heights[i][j])
            f(i,j+1,seen,heights[i][j])
            f(i,j-1,seen,heights[i][j])

            
            

        # top
        for i in range(C):
            f(0,i,pasific,heights[0][i])
        # left
        for i in range(R):
            f(i,0,pasific,heights[i][0])
        # right
        for i in range(R):
            f(i,C-1,atlantic,heights[i][C-1])
        # bottom
        for i in range(C):
            f(R-1,i,atlantic,heights[R-1][i])
        
        ans = []
        for x in atlantic:
            if x in pasific:
                ans.append(x)
        return ans