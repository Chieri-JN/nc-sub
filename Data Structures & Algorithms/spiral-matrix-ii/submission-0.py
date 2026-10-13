class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        print(matrix)
        cnt = 1
        moveDir = 0
        vStart, vEnd = 0, n-1
        hStart, hEnd = 0, n-1

        while cnt <= n**2:
            if moveDir % 2 == 0:
                # hor move
                sign = 1 - (moveDir % 4)
                for i in range(hStart, hEnd+sign, sign):
                    # print(f"hStart, hEnd, sign: {hStart}, {hEnd}, {sign}")
                    # print(f"i: {i}")
                    matrix[vStart][i] = cnt
                    cnt += 1
                hStart, hEnd = hEnd, hStart
                vStart += sign
            else:
                # vert move
                sign = 2 - (moveDir % 4)
                for i in range(vStart, vEnd+sign, sign):
                    # print(f"cnt: {cnt}")
                    # print(f"vStart, vEnd-sign: {vStart}, {vEnd-sign}")
                    # print(f"i: {i}")
                    matrix[i][hStart] = cnt
                    cnt += 1
                vStart, vEnd = vEnd, vStart
                hStart += -sign
            moveDir += 1
        return matrix