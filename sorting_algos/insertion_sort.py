def sort(nums):
    for i in range(1,len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            temp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = temp
            j = j-1


nums = [31,7,331,67,38,9]

sort(nums)
print(nums)