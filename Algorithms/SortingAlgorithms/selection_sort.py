

def selection_sort(nums):
    for i in range(len(nums)-1):
        index = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j

        if index != i:
            swap(nums, index, i)

    return nums


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


a = [3, 5, -7, -2, 3, 0, -1,]
print(selection_sort(a))