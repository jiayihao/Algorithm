def bubbleSort(self, nums: List[int]) -> List[int]:
	for i in range(len(nums) - 1, -1, -1):
		cnt = False
		for j in range(i):  
			if nums[j] > nums[j + 1]:  
				nums[j],nums[j + 1] = nums[j + 1],nums[j]
				cnt = True
		if not cnt: break
	return nums
