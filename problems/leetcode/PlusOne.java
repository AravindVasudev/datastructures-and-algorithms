class Solution {
    public int[] plusOne(int[] digits) {
        if (digits == null || digits.length == 0) {
            return null;
        }

        int carry = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i] += carry;
            if (digits[i] > 9) {
                carry = 1;
                digits[i] %= 10;
            } else {
                carry = 0;
            }
        }

        if (carry == 1) {
            int[] overFlowed = new int[digits.length + 1];

            overFlowed[0] = 1;
            for (int i = 0; i < digits.length; i++) {
                overFlowed[i + 1] = digits[i];
            }

            return overFlowed;
        }

        return digits;
    }
}
