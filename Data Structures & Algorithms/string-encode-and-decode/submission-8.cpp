class Solution {
public:

    string encode(vector<string>& strs) {
        string Answer;
        for(string i : strs){
            Answer += i + "||";
            
        }

        return Answer;
    }

    vector<string> decode(string s) {
        vector<string> Answer;
        string currStr;
        for(int i = 0;i<s.size();i++){
            if(i+1 < s.size() && s[i] == s[i+1] && s[i] == '|'){
                i += 1;
                Answer.push_back(currStr);
                currStr.clear();
                continue;
            }
            currStr.push_back(s[i]);
        }
        return Answer;
    }

};
