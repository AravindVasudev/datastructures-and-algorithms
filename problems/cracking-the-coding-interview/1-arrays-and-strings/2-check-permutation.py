from collections import defaultdict
import unittest


def isPermutation(str1: str, str2: str) -> bool:
    str1CharMap = defaultdict(int)

    for char in str1:
        str1CharMap[char] += 1

    for char in str2:
        str1CharMap[char] -= 1

    for char, occurence in str1CharMap.items():
        if occurence != 0:
            return False

    return True


class TestIsPermutation(unittest.TestCase):
    trueData = [('', ''), ('aaa', 'aaa'), ('moo', 'omo'), ('hello', 'ehlol')]
    falseData = [('', 'a'), ('a', 'b'), ('hello', 'hell'), ('aaa', 'aab')]

    def testChecksPermutationData(self):
        for test_data in self.trueData:
            self.assertTrue(isPermutation(*test_data))

        for test_data in self.falseData:
            self.assertFalse(isPermutation(*test_data))


if __name__ == '__main__':
    unittest.main()
