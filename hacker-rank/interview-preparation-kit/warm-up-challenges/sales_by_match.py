def sockMerchant(n: int, ar: list[int]) -> int:
    pairs = 0
    for color in set(ar):
        if ar.count(color) >= 2 and ar.count(color) // 2:
            pairs += 1
    return pairs


def sockMerchant2(n: int, ar: list[int]) -> int:
    return sum(ar.count(color) // 2 for color in set(ar))


if __name__ == "__main__":
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = 9

    ar2 = [1, 2, 1, 2, 1, 2, 3]
    n2 = 7

    # print(sockMerchant(n, ar))
    print(sockMerchant(n2, ar2))
