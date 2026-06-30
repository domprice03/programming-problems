#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Store key = target - nums[i] and value = i, then check if j in hashmap
        std::unordered_map<int, int> diffs;

        for (int i { 0 }; i < nums.size(); ++i) {
            int num_i { nums[i] };
            const auto it { diffs.find(num_i) };

            if (it != diffs.cend()) {
                int j = it->second;
                if (i < j)
                    return std::vector<int>{ i, j };
                else
                    return std::vector<int>{ j, i };
            }
            
            diffs[target - num_i] = i;
        }

        return std::vector<int>{ 0, 0 };
    }
};
