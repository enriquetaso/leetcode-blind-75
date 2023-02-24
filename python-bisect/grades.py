from bisect import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    index = bisect(breakpoints, score)
    print(f"For {score}: index is {index}")
    return grades[index]


if __name__ == "__main__":
    for score in [33, 99, 77, 70, 89, 90, 100]:
        print(grade(score))
    # [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
