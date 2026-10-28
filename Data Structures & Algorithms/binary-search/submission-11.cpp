#include <cstddef>  // For size_t

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int i{ 0 };
        int j{ static_cast<int>(nums.size()) - 1 };
        if (j == -1) return -1;
        int m;

        while (i <= j) {
            m = i + ((j - i) / 2);
            if (nums[m] < target)
                i = m + 1;
            else if (nums[m] > target)
                j = m - 1;
            else return m;
        }

        return -1;
    }
};
