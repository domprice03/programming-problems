class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap: dict[set, list[str]] = {}
        
        for anagram in strs:
            letters = "".join(sorted(anagram))
            hashmap[letters] = hashmap.get(letters, []) + [anagram]

        return list(hashmap.values())