from collections import Counter


def findTheDifference(s, t):
    dic = Counter(s)
    dic1 = Counter(t)
    for key in dic1:
        if key not in dic or dic[key] != dic1[key]:
            return key


if __name__ == "__main__":
    print(findTheDifference("abcd", "abcde"))
    print(findTheDifference("", "y"))
    print(findTheDifference("a", "aa"))
    print(findTheDifference("ae", "aea"))
