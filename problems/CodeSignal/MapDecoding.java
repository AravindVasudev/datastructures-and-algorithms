int mapDecoding(String message) {
    int N = message.length();
    
    if (N == 0) {
        return 1;
    }
    
    if (message.startsWith("0")) {
        return 0;
    }
    
    if (N == 1) {
        return 1;
    }
    
    int normalize = ((int) Math.pow(10, 9)) + 7;
    
    int prevPrevMax = 1;
    int prevMax = message.charAt(1) == '0' ? 0 : 1;
    int firstTwoDigits = (message.charAt(0) - '0') * 10 + (message.charAt(1) - '0');
    if (firstTwoDigits == 0 || ((firstTwoDigits > 26) && (firstTwoDigits % 10 == 0))) {
        return 0;
    }

    if (firstTwoDigits < 27 && firstTwoDigits > 9) {
        prevMax++;
    }
    
    int curMax = prevMax;
    for (int i = 2; i < N; i++) {
        curMax = message.charAt(i) == '0' ? 0 : prevMax;
        
        int twoDigitNum = (message.charAt(i - 1) - '0') * 10 + (message.charAt(i) - '0');
        if (twoDigitNum == 0 || ((twoDigitNum > 26) && (twoDigitNum % 10 == 0))) {
            return 0;
        }
        
        if (twoDigitNum < 27 && twoDigitNum > 9) {
            curMax += prevPrevMax;
        }
        
        curMax %= normalize;
        prevPrevMax = prevMax;
        prevMax = curMax;
    }
    
    return curMax;
}
