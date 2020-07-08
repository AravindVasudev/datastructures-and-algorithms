import unittest


def isUniqueWithSet(string):
    seen = set()
    for char in string:
        if char in seen:
            return False

        seen.add(char)

    return True


def isUniqueWithArray(string):
    '''
    Assumes the string is ascii
    '''
    seen = [False for i in range(128)]
    for char in string:
        value = ord(char)
        if seen[value]:
            return False

        seen[value] = True

    return True


def isUnique26Char(string):
    '''
    This assumes the string only contains from 'A' through 'Z'
    Uses 32 bit for set
    '''
    seen = 0
    offset = ord('A')
    for char in string:
        pos = 1 << (ord(char) - offset)
        if seen & pos:
            return False

        seen |= pos

    return True


def isUnqiueInefficient(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

    return True


class TestIsUnique(unittest.TestCase):
    trueData = ['', 'abcde', 'abcdefghijklmnopqrstuvwxyz', 'z']
    falseData = ['aa', 'aba', 'abcdefghijklmnopqrstuvwxyza', 'teestetst']

    def testIsUnique(self):
        for test_string in self.trueData:
            self.assertTrue(isUniqueWithSet(test_string))
            self.assertTrue(isUniqueWithArray(test_string))
            self.assertTrue(isUnique26Char(test_string))
            self.assertTrue(isUnqiueInefficient(test_string))

        for test_string in self.falseData:
            self.assertFalse(isUniqueWithSet(test_string))
            self.assertFalse(isUniqueWithArray(test_string))
            self.assertFalse(isUnique26Char(test_string))
            self.assertFalse(isUnqiueInefficient(test_string))


if __name__ == '__main__':
    unittest.main()
