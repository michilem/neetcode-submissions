class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {return false;}
        std::array<int, 26> f = {0};
        for(int i=0; i<s.size(); i++){
            int sn = s[i] - 'a';
            int tn = t[i] - 'a';
            f[sn] += 1;
            f[tn] -= 1;
        }
        return (std::array<int, 26>{0} == f);
    }
};
