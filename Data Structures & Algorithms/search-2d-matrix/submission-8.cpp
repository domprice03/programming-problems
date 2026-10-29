#include <utility>  // For std::pair

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        const auto rows{ static_cast<int>(matrix.size()) };
        const auto cols{ static_cast<int>(matrix[0].size()) };
        auto i{ 0 };
        auto j{ rows * cols - 1 };

        while (i <= j) {
            auto m{ i + (j - i) / 2 };
            auto elem{ matrix[m / cols][m % cols] };
            
            if (elem < target)
                i = m + 1;
            else if (elem > target)
                j = m - 1;
            else
                return true;
        }

        return false;
    }
};
