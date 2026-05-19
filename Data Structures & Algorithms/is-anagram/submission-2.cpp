class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> hashS;
        unordered_map<char,int> hashT;

        for(int i = 0;i<s.size();i++)hashS[s[i]]++;
        for(int i = 0;i<t.size();i++)hashT[t[i]]++;

        for(int i = 0;i<s.size();i++){
            if(hashS[s[i]] != hashT[s[i]])return false;
        }
        for(int i = 0;i<t.size();i++){
            if(hashS[t[i]] != hashT[t[i]])return false;
        }
        return true;
    }
};