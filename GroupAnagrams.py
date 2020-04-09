class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            key = list(s)
            key.sort()
            key = ''.join(key)
            anagrams[key] = [*anagrams[key],
                             s] if key in anagrams.keys() else [s]
        return [v for v in anagrams.values()]
