class Solution:
    def solveNqueen(self, n: int) -> list[list[str]]:
        col = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        res =  []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                