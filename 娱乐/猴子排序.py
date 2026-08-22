import random

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def monkey_sort_with_stats(arr):
    attempt_count = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempt_count += 1

        # 每10万次打印一次进度，避免刷屏

        if attempt_count % 100000 == 0:
            print(f"已尝试打乱 {attempt_count} 次，仍未得到有序数组...")
    print(f"总共尝试了 {attempt_count} 次打乱后完成排序")
    return arr

# 测试运行

if __name__ == "__main__":
    test_arr = [5, 2, 9, 1, 3,4,8,10,34,54,99,10,12,57,78,34,23,24]
    sorted_result = monkey_sort_with_stats(test_arr)
    print("最终排序结果:", sorted_result)