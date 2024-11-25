class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if board == [[1, 2, 3], [4, 5, 0]]:
            return 0
        k = ((1, 2, 3), (4, 5, 0))
        s = set()
        t = []
        for i in board:
            t.append(tuple(i))

        def next_seq(board):
            board = [list(i) for i in board]
            x, y = -1, -1
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 0:
                        x, y = i, j

            ans = []
            # 0 0
            if x == 0 and y == 0:
                mat1 = [row[:] for row in board]
                mat2 = [row[:] for row in board]

                mat1[0][0], mat1[0][1] = mat1[0][1], 0
                mat2[0][0], mat2[1][0] = mat2[1][0], 0
                ans = [mat1, mat2]

            if x == 0 and y == 1:
                mat1 = [row[:] for row in board]
                mat2 = [row[:] for row in board]
                mat3 = [row[:] for row in board]

                mat1[0][1], mat1[0][0] = mat1[0][0], 0
                mat2[0][1], mat2[1][1] = mat2[1][1], 0
                mat3[0][1], mat3[0][2] = mat3[0][2], 0
                ans = [mat1, mat2, mat3]

            if x == 0 and y == 2:
                mat1 = [row[:] for row in board]
                mat2 = [row[:] for row in board]

                mat1[0][2], mat1[0][1] = mat1[0][1], 0
                mat2[0][2], mat2[1][2] = mat2[1][2], 0
                ans = [mat1, mat2]

            if x == 1:
                if y == 0:
                    mat1 = [row[:] for row in board]
                    mat2 = [row[:] for row in board]

                    mat1[1][0], mat1[0][0] = mat1[0][0], 0
                    mat2[1][0], mat2[1][1] = mat2[1][1], 0
                    ans = [mat1, mat2]

                if y == 1:
                    mat1 = [row[:] for row in board]
                    mat2 = [row[:] for row in board]
                    mat3 = [row[:] for row in board]

                    # print("board", mat1, mat2, mat3)

                    mat1[1][1], mat1[1][0] = mat1[1][0], 0
                    # print("1", mat1, mat2, mat3)

                    mat2[1][1], mat2[0][1] = mat2[0][1], 0
                    # print("2", mat1, mat2, mat3)

                    mat3[1][1], mat3[1][2] = mat3[1][2], 0
                    # print("3", mat1, mat2, mat3)
                    ans = [mat1, mat2, mat3]

                if y == 2:
                    mat1 = [row[:] for row in board]
                    mat2 = [row[:] for row in board]

                    mat1[1][2], mat1[0][2] = mat1[0][2], 0
                    mat2[1][2], mat2[1][1] = mat2[1][1], 0
                    ans = [mat1, mat2]

            final = []
            for ele in ans:
                e = []
                for k in ele:
                    e.append(tuple(k))
                final.append(tuple(e))
            print(final)
            return final

        s.add(tuple(t))
        q = [tuple(t)]
        ans = 0
        while q:
            new_q = []
            for ele in q:
                pos = next_seq(ele)
                for p in pos:
                    if p not in s:
                        new_q.append(p)
                        s.add(p)
                        if p == k:
                            return ans + 1
            q = new_q
            ans += 1
        return -1
