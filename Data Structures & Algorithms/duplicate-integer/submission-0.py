class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = []
        for x in nums:
            if x in checker:
                return True
            checker.append(x)
        return False
        