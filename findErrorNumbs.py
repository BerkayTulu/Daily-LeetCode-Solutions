def findErrorNums(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        duplicate = sum(nums) - sum(set(nums))
        missing = expected_sum - actual_sum + duplicate
        return [duplicate, missing]

numbs = [2,2]
print(findErrorNums(numbs))