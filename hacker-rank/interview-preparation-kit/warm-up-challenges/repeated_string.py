def repeatedString(s, n):
    target = "a"

    left_letters = 0
    for i in range(n % len(s)):
        if s[i] == target:
            left_letters += 1

    return (n // len(s)) * s.count(target) + left_letters


def repeatedString2(s, n):
    target = "a"
    if len(s) == 0:
        return 0
    if len(s) == 1 and s == target:
        return n
    new_str = s * n
    return new_str[:n].count(target)


if __name__ == "__main__":
    print(repeatedString2("a", 1000000000000))

    # print(repeatedString2("ab", 10))

    result_test2 = 7
    test2 = repeatedString2("aba", 10)
    if test2 == result_test2:
        print("Test 2 passed")
    else:
        print("Test 2 wrong result=", test2)
    # print(repeatedString2("abcac", 10))
    # print(repeatedString2("abcac", 11))
