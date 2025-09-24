from collections import deque
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c, 0, set([(r, c)])))
            
            while queue:
                x, y, idx, visited = queue.popleft()
                if idx == len(word) - 1:
                    return True
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and
                        (nx, ny) not in visited and
                        board[nx][ny] == word[idx + 1]):
                        queue.append((nx, ny, idx + 1, visited | {(nx, ny)}))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if bfs(i, j):
                        return True
        return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

sol = Solution()
print(sol.exist(board, "ABCCED"))
print(sol.exist(board, "ABCB"))