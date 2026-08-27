"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？
"""
# 解法一（暴力解法，时间复杂度 O(n²)，空间复杂度：O(1)）：
def twe_sum1(nums,target):
    # 获取列表nums的长度
    n = len(nums)
    for i in range(n): # 第一次遍历
        for j in range(i + 1,n): # 第二次遍历
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

# 解法二 （哈希表 ---> Python中哈希表就是字典,时间复杂度 O(n)，空间复杂度：O(n)）
def twe_sum2(nums,target):
    cache = {}
    # 把数据存入哈希表
    for i,item in enumerate(nums):
        cache[item] = i
    # 遍历 nums 中的所有元素，求 target - item 的值，在去哈希表查找对应下标
    for i,item in enumerate(nums):
        other = target - item
        if other in cache and cache[other] != i: # 不能使用两次相同的元素
            return [i,cache[other]]
    return []

# 解法三 （哈希表优化 - 边遍历边记录哈希表，时间复杂度 O(n)，空间复杂度：O(n)）
def twe_sum3(nums,target):
    cache = {}
    for i,item in enumerate(nums):
        other = target - item
        if other in cache:
            return [i,cache[other]]
        else:
            cache[item] = i
    return []
# 测试
nums = [2,7,11,15]
target = 9
print(twe_sum1(nums,target))

nums = [3,2,4]
target = 6
print(twe_sum3(nums,target))

nums = [3,3]
target = 6
print(twe_sum3(nums,target))