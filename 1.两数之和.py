#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, num in enumerate(nums):
            second_num = target - num
            if second_num in dict:
                return [dict[second_num], index]
            dict[num] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
