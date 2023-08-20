class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        limit_index = len(numbers)
        for i in range(0, len(numbers)):
            if(numbers[i] > target):
                limit_index = i + 1
        for i in range(0, limit_index):
            if numbers[i] == numbers[i+1] and numbers[i] + numbers[i+1] != target:
                continue
            for j in range(i+1, limit_index):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return [-1, -1]
