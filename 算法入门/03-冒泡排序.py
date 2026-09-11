"""
冒泡排序：
    重复遍历要排序的数组，每次比较相邻两个元素：
    如果前一个比后一个大，就交换它们；
    这样每一轮结束后，最大的元素会像气泡一样“浮”到数组末尾。
"""
def bubblesort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0,n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j+1] = nums[j + 1],nums[j]
    return nums

# 测试
nums = [23,45,11,32,22,34,45,68,12,5]
print(bubblesort(nums))