class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            curr = nums[i]
            needed = target - curr

            if needed in seen:
                return [seen[needed], i]
            seen[curr] = i