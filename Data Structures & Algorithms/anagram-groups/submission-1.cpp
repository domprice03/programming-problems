#include <array>
#include <string>
#include <map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::array<int, 26>, std::vector<std::string>> mapping{ };
        for (const auto& str : strs) {
            std::array<int, 26> char_counts{ };
            for (const auto& chr : str) {
                ++char_counts[static_cast<int>(chr) - static_cast<int>('a')];
            }
            mapping[char_counts].push_back(str);
        }
        std::vector<std::vector<std::string>> res{ };
        for (const auto& k_v_pair : mapping) {
            res.push_back(k_v_pair.second);
        }
        return res;
    }
};
