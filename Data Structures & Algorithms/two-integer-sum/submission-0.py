class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash seen nums, check for complement
        # for i, see if seen int = target - i

        seen = {}

        for idx, val in enumerate(nums):
            goal = target - val

            if goal in seen:
                return [seen[goal], idx]

            seen[val] = idx




        # brute solution seems to check every number with every other
        # this is O(n^2), quite slow
        # let's code it

        # result = []

        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             result += [i, j]
        
        # return result
        