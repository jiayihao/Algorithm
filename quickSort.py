def quickSort(self, nums: List[int], left: int, right: int) -> None:
     # check if the recursion can be terminated
     if left >= right: return

     l, r = left, right
     pivot = left

     # add random to reach o(nlogn)
     rd = random.randint(left, right)
     nums[rd], nums[l] = nums[l], nums[rd]

     while l < r:
         # make sure it is >= or <= to make it moving
         while l < r and nums[r] >= nums[pivot]:
             r -= 1
         while l < r and nums[l] <= nums[pivot]:
             l += 1
         # when l and r are not crossing then swap the item
         nums[l], nums[r] = nums[r], nums[l]
     # if stop somewhere in the middle, swap!
     nums[pivot], nums[r] = nums[r], nums[pivot]

     # it is a implicit pre-order dfs
     self.quickSort(nums, left, r - 1)
     self.quickSort(nums, r + 1, right)
