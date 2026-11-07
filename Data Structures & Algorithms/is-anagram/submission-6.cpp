class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        std::vector<int> count(26, 0);
        for(size_t i=0; i < s.size(); i++){
            char cs = s[i];
            char ts = t[i];
            count[cs - 'a'] += 1;
            count[ts - 'a'] -= 1;
        }
        return count == std::vector<int> (26, 0);
    }
};
