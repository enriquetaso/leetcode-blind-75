# https://www.youtube.com/watch?v=vzdNOK2oB2E


from collections import defaultdict
from typing import List


def groupAnagrams(strs):
    """
    Time complexity: O(n^2)
    Memory complexity O(n)
    """
    response = defaultdict(list)
    for word in strs:
        count = [0] * 26  # a..z
        for char in word:
            count[ord(char) - ord("a")] += 1

        response[tuple(count)].append(word)
    return response.values()


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    """Group anagram using sorting

    defaultdict
    ===========
    A common problem that you can face when working with Python
    dictionaries is to try to access or modify keys that don’t
    exist in the dictionary. This will raise a KeyError and break
    up your code execution. To handle these kinds of situations,
    the standard library provides the Python defaultdict type, a
    dictionary-like class that’s available for you in collections.

    The Python defaultdict type behaves almost exactly like a regular
    Python dictionary, but if you try to access or modify a missing
    key, then defaultdict will automatically create the key and generate
    a default value for it. This makes defaultdict a valuable option
    for handling missing keys in dictionaries.

    Time complexity: O(nlogn)
    Memory complexity: O(n)
    """
    groups_of_anagrams = defaultdict(list)

    for word in strs:
        # sorted() built-in function builds a new sorted list
        # from an iterable (in this case str).
        groups_of_anagrams[tuple(sorted(word))].append(word)
    return groups_of_anagrams.values()


if __name__ == "__main__":
    print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams2([""]))
    print(groupAnagrams2(["a"]))
