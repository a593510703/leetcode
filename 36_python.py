class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
#check r
        Tmp = []
        for Tmp in board:
            vis = [0] * 10
            for x in Tmp:
                if x != 0:
                    vis[x] += 1
            for x in vis:
                if x > 1:
                    return False
#check c
        for i in range(9):
            Tmp = []
            for j in range(9):
                Tmp.append(board[j][i])
            vis = [0] * 10
            for x in Tmp:
                if x != 0:
                    vis[x] += 1
            for x in vis:
                if x > 1:
                    return False

#check 1
        vis = [0] * 10
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(3):
            for j in range(3, 6):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(3):
            for j in range(6, 9):
                print(board[i][j])
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(3, 6):
            for j in range(3):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(6, 9):
            for j in range(3):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False
        vis = [0] * 10
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] != 0:
                    vis[board[i][j]] += 1
                for x in vis:
                    if x > 1:
                        return False

        return True