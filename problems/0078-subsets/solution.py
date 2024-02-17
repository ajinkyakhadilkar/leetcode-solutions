class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def find_subsets(i) :
            if(i == len(nums)) :
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            find_subsets(i+1)

            subset.pop()
            find_subsets(i+1)

        find_subsets(0)
        return res
