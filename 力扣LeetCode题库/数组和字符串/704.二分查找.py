"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。
你必须编写一个具有 O(log n) 时间复杂度的算法。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""
# 二分查找 - O(log n) 时间复杂度
def search(nums, target):
    # 设置[left,right)区间，有设区间一般都左闭右开
    left = 0
    right = len(nums)
    mid = (left + right) // 2
    while left < right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # left是闭要考虑，left = mid会把排除的nums[mid]重新考虑回来，所有要用left = mid + 1
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        mid = (left + right) // 2
    return -1

"""
                O(n)                log n
n = 100         100次               7次
n = 1万         1万次               14次 
n = 100万       100万次             20次
80亿            80亿次              33次 
log n 的复杂度的算法是十分优秀的算法
"""
