import collections


def firstUniqChar(self, s: str) -> int:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # where, n = len(s)
    count = collections.Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


def firstUniqChar2(self, s: str) -> int:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # where, n = len(s)
    count = [0] * 26
    for c in s:
        count[ord(c) - ord("a")] += 1
    for i, c in enumerate(s):
        if count[ord(c) - ord("a")] == 1:
            return i
    return -1


def firstUniqChar3(s: str) -> int:
    """Hits Time Limit Exceeded when s is too big."""
    unique_chars = [c for c in s if s.count(c) == 1]
    for i in range(len(s)):
        if s[i] in unique_chars:
            return i
    return -1


if __name__ == "__main__":
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aabb"))
