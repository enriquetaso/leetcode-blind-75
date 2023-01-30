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

from typing import Counter


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


def isAnagram3(s: str, t: str) -> bool:
    # Can you solve the problem with O(1) memory?
    # Yes, sorting the strings.
    # Depending on the sorting algorithm, but
    # generally speaking, it is less effective
    # than the first two options.
    # Perhaps you could create your own sorting
    # algorithm.
    return sorted(s) == sorted(t)
