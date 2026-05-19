class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for(string it : strs){
            encoded += to_string(it.size()) + '#' + 'A';
            for(char i : it)encoded += i;
        cout << it.size() << endl;
        }
        cout << encoded << endl;
        return encoded;
    }

    vector<string> decode(string s) {
        int index = 0;
        vector<string> decoded;
        if(s.size() < 1)return decoded;
        while(index < s.size()-1){
            string temp;
            int tempSize = 0;
            while(s[index] != '#'){
                int digit = int(s[index]-'0');
                cout << digit << " " << index << "-";
                tempSize = 10*tempSize + digit;
                index++;
            }
            
            index+= 2;
        while(temp.size() < tempSize){
            temp += s[index];
            if(index < s.size()-1)index++;
            else break;
        }
            decoded.push_back(temp);
        }
        return decoded;
    }
};
