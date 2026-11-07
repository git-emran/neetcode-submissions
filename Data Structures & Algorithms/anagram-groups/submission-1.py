class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            cleanSort = ''.join(sorted(s))
            result[cleanSort].append(s)
        
        return list(result.values())