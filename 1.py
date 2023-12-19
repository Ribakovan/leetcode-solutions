class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        known_nums = {}
        for i, num in enumerate(nums):
            required = target - num
            if required in known_nums:
                return [known_nums[required], i]
            known_nums[num] = i