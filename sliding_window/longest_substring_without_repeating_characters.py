# Given a string s, find the length of the longest substring without repeating characters.
# https://www.youtube.com/watch?v=wiGpQwVHdE0


def lengthOfLongestSubstring(s):
    """
    :type s: str
    """
    char_set = set()
    left_index = 0
    result = 0

    for right_index in range(len(s)):
        while s[right_index] in char_set:
            char_set.remove(s[left_index])
            left_index += 1
        char_set.add(s[right_index])
        print(
            f"right {right_index}: {s[right_index]}, left {left_index}: {s[left_index]}, result {result} o {right_index - left_index + 1}, set {char_set}"
        )
        result = max(result, right_index - left_index + 1)
    return result
