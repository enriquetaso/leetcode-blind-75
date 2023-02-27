from collections import deque


def countingValleys(steps: int, path: str) -> int:
    valleys = floor = 0
    steps = {"U": 1, "D": -1}

    for step in path:
        floor += steps[step]
        if floor == 0 and step == "U":
            valleys += 1
    return valleys


if __name__ == "__main__":
    steps1 = 8
    path1 = "DDUUUUDD"
    result = countingValleys(steps1, path1)
    if result == 1:
        print("FINE")
    else:
        print("WRONG")

    steps2 = 8
    path2 = "UDDDUDUU"
    result2 = countingValleys(steps2, path2)
    if result2 == 1:
        print("FINE")
    else:
        print("WRONG")
