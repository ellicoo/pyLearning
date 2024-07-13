"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。


示例 1：

输入：nums = [1,2,3,1]
输出：true
示例 2：

输入：nums = [1,2,3,4]
输出：false
示例 3：

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                return True
            # 如果不在则添加映射
            count[nums[i]] = 1
        return False
