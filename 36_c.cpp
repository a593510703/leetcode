bool judge(vector <int>& x) {
    int vis[10];
    memset(vis, 0, sizeof(vis));
    for (int i = 0; i < 9; i++)
        if (x[i] != 0)
            vis[x[i]]++;
    for (int i = 0; i < 10; i++)
        if (vis[i] > 1)
            return true;
    return false;
}
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector <vector <int>> Board;
        vector <int> Tmp;
        Board.resize(9);
        for (int i = 0; i < 9; i++)
            Board[i].resize(9);
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                Board[i][j] = board[i][j] == '.' ? 0 : board[i][j] - '0';
        for (int i = 0; i < 9; i++)
            if (judge(Board[i]))
                return false;
        for (int i = 0; i < 9; i++) {
            Tmp.clear();
            for (int j = 0; j < 9; j++)
                Tmp.push_back(Board[j][i]);
            if (judge(Tmp))
                return false;
        }
        Tmp.clear();
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 0; i < 3; i++)
            for (int j = 3; j < 6; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 0; i < 3; i++)
            for (int j = 6; j < 9; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 3; i < 6; i++)
            for (int j = 0; j < 3; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 3; i < 6; i++)
            for (int j = 3; j < 6; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 3; i < 6; i++)
            for (int j = 6; j < 9; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 6; i < 9; i++)
            for (int j = 0; j < 3; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 6; i < 9; i++)
            for (int j = 3; j < 6; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        Tmp.clear();
        for (int i = 6; i < 9; i++)
            for (int j = 6; j < 9; j++) {
                Tmp.push_back(Board[i][j]);
            }
        if (judge(Tmp))
            return false;
        return true;
    }
};
