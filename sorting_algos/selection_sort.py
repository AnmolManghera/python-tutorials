def sort(nums):
    for i in range(0,len(nums)-1):
        min_idx = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        temp = nums[min_idx]
        nums[min_idx] = nums[i]
        nums[i] = temp


nums = [31,7,331,67,38,9]

sort(nums)
print(nums)