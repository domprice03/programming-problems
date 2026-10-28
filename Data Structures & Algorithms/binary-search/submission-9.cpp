#include <cstddef>  // For size_t

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len{ static_cast<int>(nums.size()) };
        if (len == 0) return -1;

        int i{ 0 };
        int j{ len - 1 };
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
