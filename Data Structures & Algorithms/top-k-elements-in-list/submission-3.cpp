class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        vector<vector<int>> count(nums.size()+1);

        for(auto num : nums){
            freq[num]++;
        }
        for(auto& [key, val] : freq){
            count[val].push_back(key);
        }
        vector<int> out;
        for(int i=count.size()-1; i>0; i--){
            for(int c : count[i]){
                out.push_back(c);
                if(out.size() == k){
                    return out;
                }
            }
        }
        return out;
    }
};
