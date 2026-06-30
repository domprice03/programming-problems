#include <array>
#include <cstddef>   // For std:size_t
#include <string_view>
#include <utility>  // For std::pair

constexpr short g_alphabet_length { 26 };

class Solution {
public:
    bool isAnagram(std::string_view s, std::string_view t) {
        if (s.length() != t.length()) return false;

        const std::size_t length { s.length() };
        std::array<std::size_t, g_alphabet_length> counts { 0 };

        for (std::size_t i = 0; i < length; ++i) {
            ++counts[s[i] - 'a'];
            --counts[t[i] - 'a'];
        }

        for (const auto& count : counts) {
            if (count != 0) return false;
        }

        return true;
    }
};
