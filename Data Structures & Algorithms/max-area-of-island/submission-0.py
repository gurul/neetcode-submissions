class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        bfs
            go through all directions
            update visit
            but also track max
            size update 

        visit set

        nested for loop
            look for 1s
                bfs

        1 1 0 0
        1 0 0 0
        0 0 0 1

        rows = 3
        cols = 4
        
        visit {}
        """

        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col) -> int:
            q = collections.deque()
            q.append((row,col))
            directions = [[-1, 0], [1,0], [0,1], [0,-1]]
            size = 1
            
            while q:
                currR, currC = q.popleft()
                for dr, dc in directions:
                    r = currR + dr
                    c = currC + dc
                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == 1) and ((r,c) not in visit):
                        size+=1
                        visit.add((r,c))
                        q.append((r,c))
            
            return size

        maxSize = 0 

        for i in range(rows):
            for j in range(cols):
                visit.add((i,j))
                if grid[i][j] == 1:
                    maxSize = max(maxSize, bfs(i,j))
        return maxSize
             