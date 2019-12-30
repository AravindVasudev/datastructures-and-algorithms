class Solution {
    // Without using long to handle overflow
    public int myAtoi(String str) {
        char[] strArr = str.toCharArray();
        int N = strArr.length;

        if (N == 0) return 0;

        int i = 0;
        // skip whitespace
        while (i < N && strArr[i] == ' ') i++;

        if (i >= N) return 0; //out of bound

        boolean isNeg = false;
        if (strArr[i] == '+') {
            i++;
        } else if (strArr[i] == '-') {
            isNeg = true;
            i++;
        }

        int cur = -1;
        if (i < N) cur = strArr[i] - '0';
        if (cur < 0 && cur > 9) return 0;

        int num = 0, prev = 0;
        boolean overFlowFlag = false;
        while (i < N && cur >= 0 && cur < 10) {
            num *= 10;

            if (prev != (num / 10)) { // overflow
                overFlowFlag = true;
                num = Integer.MAX_VALUE;
                break;
            }

            prev = num;
            num += cur;

            if (prev != (num - cur) || prev > num) {
                overFlowFlag = true;
                num = Integer.MAX_VALUE;
                break;
            }

            i++;
            if (i < N) cur = strArr[i] - '0';
            prev = num;
        }

        if (isNeg) {
            if (overFlowFlag) num = Integer.MIN_VALUE;
            else num *= -1;
        }

        return num;
    }
}
