"""
back tracking

iterate through each start letter, 
    - use idx of char were lookign for 
    - pass in set of seen positions so we dont repeat
    - if we find all the letters return true 
    - otherwise return false
    word[idx] is the letter we are currently looking for
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        n, m = len(board), len(board[0])
        wLen = len(word)

        def backtrack(idx, seenPos, currPos):
            if idx == wLen: 
                return True  # might not be the right stagte 
            else: 
                i, j = currPos
                # print(f"At letter {board[i][j]} at i:{i}, j:{j}")
                for v, h in moves:
                    newI, newJ = v + i, j + h
                    validI = 0 <= newI < n
                    validJ = 0 <= newJ < m
                    if validI and validJ and (newI,newJ) not in seenPos:
                        letter = board[newI][newJ]
                        if letter == word[idx]:
                            seenPos.add((newI,newJ))
                            if backtrack(idx + 1, seenPos, (newI,newJ)):
                                return True
                            seenPos.remove((newI,newJ))

                return False


        

        seen = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    seen.add((i,j))
                    if backtrack(1, seen, (i,j)):
                        return True
                    seen.remove((i,j))

        return False