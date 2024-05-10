

def insertion_sort(nums):

    for i in range(len(nums)):

        j = i

        while j > 0 and nums[j-1] > nums[j]:
            swap(nums, j, j-1)
            j = j-1

    return nums


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


a = [9,8,2,-1,-8,6,3,0]
print(insertion_sort(a))