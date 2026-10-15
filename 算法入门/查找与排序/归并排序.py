# 分治策略（Divide and Conquer，分而治之）是一种重要算法设计思想：
# 把一个复杂问题分解成若干个规模较小、结构与原问题相同的子问题，分别求解，再合并子问题的解，得到原问题的解。
# 归并排序是递归算法，思路是将数据表持续分裂为两半，对半分别进行排序
#   递归的基本结束条件是：数据表仅有1各数据项，自然是排好序的；
#   缩小规模：将数据表分裂为相等的两半，规模减为原来的二分之一；
#   调用自身：将两半分别调用自身排序，然后将分别排好序的两半进行归并，得到排好的数据表

def merge_sort(lst):
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题，并递归调用
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])  # 左半部分排好序
    right = merge_sort(lst[middle:])  # 右半部分排好序

    # 合并左右半部分，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged

if __name__ == "__main__":
    arr = [8,1,2,4,3,6,9,5,7]
    print(merge_sort(arr))