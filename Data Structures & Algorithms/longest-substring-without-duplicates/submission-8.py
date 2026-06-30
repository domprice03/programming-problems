class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length in (0, 1):
            return length
        
        left = 0
        right = 1
        longest = 1
        seen = set(s[left:right])

        while left < right and right < length:
            right_char = s[right]

            while right_char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(right_char)
            right += 1
            longest = max(longest, right - left)

        return longest