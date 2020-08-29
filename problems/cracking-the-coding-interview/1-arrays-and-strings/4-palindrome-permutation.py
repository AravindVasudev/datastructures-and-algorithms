from collections import defaultdict


def palindrome_permutation(string):
    string = string.lower().replace(' ', '')
    strMap = defaultdict(int)
    for char in string:
        strMap[char] += 1

    hasUniqueChar = False
    for occurence in strMap.values():
        if occurence & 1:
            if hasUniqueChar:
                return False

                hasUniqueChar = True

    return True


if __name__ == '__main__':
    print(palindrome_permutation('Tact Coa'))
