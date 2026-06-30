#include <string_view>
#include <unordered_map>
#include <utility>

class Solution {
public:
    bool isAnagram(std::string_view s, std::string_view t) {
        std::unordered_map<char, int> s_char_counts;
        std::unordered_map<char, int> t_char_counts;

        for (const char s_char : s) {
            s_char_counts[s_char]++;
            t_char_counts[s_char];
        }
        for (const char t_char : t) {
            t_char_counts[t_char]++;
            s_char_counts[t_char];
        }

        for (const std::pair<const char, int>& s_pair : s_char_counts) {
            if (t_char_counts[s_pair.first] != s_pair.second) {
                return false;
            }
        }

        return true;
    }
};
