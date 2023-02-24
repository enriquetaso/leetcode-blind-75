# https://www.youtube.com/watch?v=9UtInBqnCgA&feature=youtu.be
# Given two strings s and t, return true if t is
# an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by
# rearranging the letters of a different word or
# phrase, typically using all the original
# letters exactly once.
#
# Input: s = "anagram", t = "nagaram"
# Output: true

# Follow up :

# What if the inputs contain unicode characters?
# How would you adapt your solution to such case?

# Answer : Use a hash table instead of a fixed
# size counter. Imagine allocating a large size
# array to fit the entire range of unicode characters,
# which could go up to more than 1 million. A hash
# table is a more generic solution and could adapt
# to any range of characters.

import time
from typing import Counter


def timer_func(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished in {func.__name__}: {(end - start)*1000000:.1f}ms")
        return result

    return wrapper


@timer_func
def isAnagram(s: str, t: str) -> bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for index in range(len(s)):
        countS[s[index]] = 1 + countS.get(s[index], 0)
        countT[t[index]] = 1 + countT.get(t[index], 0)
    for c in countS:
        if countS.get(c, False) != countT.get(c, False):
            return False
    return True


def isAnagram2(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


@timer_func
def isAnagram3(s: str, t: str) -> bool:
    """Can you solve the problem with O(1) memory?

    Yes, using"""
    if len(s) != len(t):
        return False

    # Can you solve the problem with O(1) memory?
    # Yes, sorting the strings.
    # Depending on the sorting algorithm, but
    # generally speaking, it is less effective
    # than the first two options.
    # Perhaps you could create your    # print(isAnagram(s, t))
    # print(isAnagram3(s, t))
    # print(isAnagram4(s, t)) own sorting
    # algorithm.
    return sorted(s) == sorted(t)


@timer_func
def isAnagram4(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for c in s:
        if s.count(c) != t.count(c):
            return False
    return True


@timer_func
def isAnagram5(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    letters = [0] * 26  # [a .. z]
    lettert = [0] * 26  # [a .. z]

    for i in range(len(s)):
        letters[ord(s[i]) - ord("a")] += 1
        lettert[ord(t[i]) - ord("a")] += 1

    return letters == lettert


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    print(isAnagram3(s, t))
    print(isAnagram4(s, t))
    print(isAnagram5(s, t))
    print(isAnagram4("eat", "eats"))
