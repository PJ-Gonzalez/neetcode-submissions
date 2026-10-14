class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        _subsets = []
        subset = []

        def rec_subset(subset, index):
            if index == len(nums):
                _subsets.append(subset.copy())
                return
                
            # Leave number
            rec_subset(subset, index +1)
            # Pull out number
            subset.append(nums[index])
            rec_subset(subset, index +1)
            subset.pop()
            
        rec_subset(subset, 0)
        return _subsets
