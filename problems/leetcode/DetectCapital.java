// https://leetcode.com/problems/detect-capital/
class Solution {
    public boolean detectCapitalUse(String word) {
        if (word == null || word.length() < 2) {
            return true;
        }

        char[] wordArr = word.toCharArray();
        boolean isUpperCase = isCapital(wordArr[0]) && isCapital(wordArr[1]);
        for (int i = 1; i < wordArr.length; i++) {
            if (isCapital(wordArr[i]) != isUpperCase) {
                return false;
            }
        }

        return true;
    }

    private boolean isCapital(char c) {
        int charOffset = c - 'A';
        return charOffset >= 0 && charOffset < 26;
    }
}
