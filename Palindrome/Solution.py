from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        sorted_nums=sorted(nums)
        print(sorted_nums)
        len_nums = len(sorted_nums)
        print(len_nums)
        for i in range(0, len_nums-1):
            print(i)
            print(nums[i])
            print(nums[i + 1])
            if sorted_nums[i] == nums[i + 1]:
                return True
        return False



s = Solution()
r=s.containsDuplicate([1, 2, 3, 1])
print(r)