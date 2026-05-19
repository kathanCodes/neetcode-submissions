class Solution {
public:
    bool isValid(string s) {
        string valid;
        for(char i : s){
            if(i == ']' && *valid.rbegin() == '[')valid.pop_back();
            else if(i == '}' && *valid.rbegin()== '{')valid.pop_back();
            else if(i == ')' && *valid.rbegin()== '(')valid.pop_back();
            else valid.push_back(i);
        }
        return valid.empty();
    }
};
