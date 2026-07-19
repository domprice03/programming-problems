#include <algorithm>    // For std::heap functions
#include <functional>   // For anonymous comparator

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        const std::function<bool(int, int)> max_cmp = [](int a, int b) { return a < b; };
        std::make_heap(nums.begin(), nums.end(), max_cmp);
        
        for (int i{ 0 }; i < k-1; ++i) {
            std::pop_heap(nums.begin(), nums.end(), max_cmp);
            nums.pop_back();
        }

        return nums[0];
    }
};
