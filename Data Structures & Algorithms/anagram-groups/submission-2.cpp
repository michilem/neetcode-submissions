class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> lookup;
        for(string& s:strs) {
            std::array<int, 26> freq = {0};
            for (char& c:s) {
                freq[c - 'a']++;
            }
            string k = "";
            for (int& cnt:freq){
                k += std::to_string(cnt) + ',';
            }
            lookup[k].push_back(s);
        }
        vector<vector<string>> out;
        for (auto& kv : lookup) {
            out.push_back(kv.second);
        }
        return out;
    }
};
