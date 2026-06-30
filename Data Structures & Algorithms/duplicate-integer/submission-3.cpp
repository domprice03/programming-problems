#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (const int& num : nums) {
            if (seen.contains(num)) {
                return true;
            } else {
                seen.insert(num);
            }
        }

        return false;
    }
};