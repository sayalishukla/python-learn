"""
A two-pointer approach could be helpful here.
The idea would be to have one pointer for iterating the array
and another pointer that just works on the non-zero elements of the array.

Can be use in traversal and comparison
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[i],nums[z]=nums[z],nums[i]
                z+=1


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,3,0,5,0,10]
    sol.moveZeroes(nums)
    print(nums)
    nums1 = [5, 4, 0, 10, 7, 0, 1]
    sol.moveZeroes(nums1)
    print(nums1)
