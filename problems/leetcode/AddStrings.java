// https://leetcode.com/problems/add-strings/
class Solution {
    public String addStrings(String num1, String num2) {
        String longStr;
        String shortStr;
        if (num1.length() > num2.length()) {
            longStr = num1;
            shortStr = num2;
        } else {
            longStr = num2;
            shortStr = num1;
        }
        
        char[] longArr = longStr.toCharArray();
        char[] shortArr = shortStr.toCharArray();
        
        int longEnd = longArr.length - 1;
        int shortEnd = shortArr.length -  1;
        
        int carry = 0;
        while (longEnd >= 0 && shortEnd >= 0) {
            int curTotal = longArr[longEnd] + shortArr[shortEnd] + carry - (2 * '0');
            carry = 0;

            if (curTotal > 9) {
                carry = 1;
                curTotal -= 10;
            }
            
            longArr[longEnd] = (char)(curTotal + '0');

            longEnd--;
            shortEnd--;
        }
        
        while (longEnd >= 0 && carry > 0) {
            int curTotal = longArr[longEnd] + carry - '0';
            carry = 0;

            if (curTotal > 9) {
                carry = 1;
                curTotal -= 10;
            }
            
            longArr[longEnd] = (char)(curTotal + '0');
            longEnd--;
        }
        
        String sum = new String(longArr);

        if (carry > 0) {
            sum = Integer.toString(carry) + sum;
        }
        
        return sum;
    }
}
