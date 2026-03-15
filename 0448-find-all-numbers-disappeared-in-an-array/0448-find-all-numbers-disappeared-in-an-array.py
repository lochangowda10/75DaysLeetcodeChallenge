class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        o_list = set()
        nums = set(nums)
        for i in range(1,n+1):
            if i not in nums:
                o_list.add(i)
        o_list = list(o_list)
        return o_list