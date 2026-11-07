class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        most_frequent = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_frequent = max(most_frequent, count[s[r]])

            while (r-l+1) - most_frequent > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            res = max(res, r-l+1)
        return res