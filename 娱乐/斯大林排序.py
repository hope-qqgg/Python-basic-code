def stalin_sort(arr):
    if not arr:  # 处理空数组边界情况
        return []
    sorted_arr = [arr[0]]
    for num in arr[1:]:

        # 只保留大于等于序列最后一个元素的数
        if num >= sorted_arr[-1]:
            sorted_arr.append(num)
    return sorted_arr

# 测试
if __name__ == "__main__":
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print("原数组:", test_arr)
    print("斯大林排序结果:", stalin_sort(test_arr))

    # 输出: 原数组: [3, 1, 4, 1, 5, 9, 2, 6]

    # 排序后: [3, 4, 5, 9]
