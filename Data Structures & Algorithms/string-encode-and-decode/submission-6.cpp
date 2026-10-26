class Solution {
public:

    string encode(vector<string>& strs) {
        char sep = '#';
        string out = "";
        for(auto str : strs){
            out += to_string(str.size()) + sep + str;
        }
        return out;
    }

    vector<string> decode(string s) {
        vector<string> out;
        char sep = '#';
        string l = "";// = s.substr(0,1);
        for(int i=0; i<s.size(); i++){
            if(s[i] == sep){
                
                out.push_back(s.substr(i+1, stoi(l)));
                i = i + stoi(l);
                l = "";
                
            }
            else{
                l += s[i];
            }
        }
        return out;
    }
};
