class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def build_freq_map(string: str) -> dict[str, int]:

            _freq: dict[str, int] = {}

            for c in string:
                if c not in _freq:
                    _freq[c] = 1
                else :
                    _freq[c] +=1
            return _freq
        
        s_freq= build_freq_map(s)
        t_freq= build_freq_map(t)

        for c in s_freq:
            if c not in t_freq:
                return False
            if s_freq[c] != t_freq[c]:
                return False
        
        return True
