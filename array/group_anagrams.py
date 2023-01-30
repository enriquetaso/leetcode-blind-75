# https://www.youtube.com/watch?v=vzdNOK2oB2E
from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    response = defaultdict(list)
    for word in strs:
        count = [0] * 26  # a..z
        for char in word:
            count[ord(char) - ord("a")] += 1

        response[tuple(count)].append(word)
    return response.values()
