class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for s_i, t_i in zip(s, t):
            s_map[s_i] = s_map.get(s_i, 0) + 1
            t_map[t_i] = t_map.get(t_i, 0) + 1
        
        for s_k, s_v in s_map.items():
            if t_map.get(s_k) != s_v:
                return False
        
        return True