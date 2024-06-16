def sort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(0,i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [31,7,331,67,38,9]

sort(nums)
print(nums)