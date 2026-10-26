class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        int start = nums[0];
        int l = nums.size();

        std::unordered_map<int, int> lookup;

        for(int i=0; i<l; i++){
            int s = target - nums[i];
            if(lookup.count(nums[i])){
                return {lookup[nums[i]], i};
            }

            lookup[s] = i;
        }

        
        
    }
};
