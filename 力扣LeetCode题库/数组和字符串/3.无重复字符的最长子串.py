"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 10⁵
s 由英文字母、数字、符号和空格组成
"""
# 滑动窗口（快慢指针，复杂度O(n)）
def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    my_set = set()
    max_len = 0
    while right < len(s):
        if s[right] in my_set:
            my_set.remove(s[left])
            left += 1
        else:
            my_set.add(s[right])
            max_len = max(max_len, len(my_set))
            right += 1
    return max_len

# 测试
s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))