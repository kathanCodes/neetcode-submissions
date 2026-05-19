class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        for(int i = 0;i<board.size();i++){
            vector<int> col(board.size(),0);
            vector<int> row(board.size(),0);
            for(int j = 0;j<board.size();j++){
                if(board[i][j] != '.')row[int(board[i][j]-'1')]++;
                if(board[j][i] != '.')col[(int(board[j][i]-'1'))]++;
                if(row[int(board[i][j]-'1')] > 1 || col[(int(board[j][i]-'1'))] > 1)return false;
            }
        }
        for(int centerPointX = 1;centerPointX < board.size()-1;centerPointX += 3){
            for(int centerPointY = 1;centerPointY < board.size()-1;centerPointY += 3){
                vector<int> square(9,0);
                for(int i = centerPointX-1;i<centerPointX+2;i++){
                    for(int j = centerPointY-1;j<centerPointY+2;j++){
                        if(board[i][j] != '.')square[int(board[i][j]-'1')]++;
                        if(square[int(board[i][j]-'1')] > 1)return false;
                    }
                }
            }
        }
            
        
        
        return true;
    }
};
