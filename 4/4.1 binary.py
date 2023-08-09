a = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 0
high = len(nums) - 1
index = None
while (low <= high) and index is None:
    mid = (low + high) // 2
    if nums[mid] == a:
        index = mid
    else:
        if a < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
print('Элемент находится под индексом', index)
