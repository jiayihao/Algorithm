def insertSort(self, nums: List[int]) -> List[int]:

    length = len(nums) 
    for i in range(1, length):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break
    return nums
