def mergeSort(self, nums: List[int], left: int, right: int) -> None:

	if left >= right: return
	mid = left + (right - left) // 2
	self.mergeSort(nums, left, mid)
	self.mergeSort(nums, mid + 1, right)
	self.mergeSortedArray(nums, left, mid, right)

def mergeSortedArray(self, nums: List[int], left: int, mid: int, right: int) -> None:
	
	tmp = []
	# a and b are two walkers/pointers
	a, b = left, mid + 1
	while a <= mid and b <= right:
		if nums[a] <= nums[b]:
			tmp.append(nums[a])
			a += 1
		else:
			tmp.append(nums[b])
			b += 1
	if a <= mid:
		tmp.extend(nums[a:mid + 1])
	else:
		tmp.extend(nums[b:right + 1])
	nums[left:right + 1] = tmp.copy()
	
