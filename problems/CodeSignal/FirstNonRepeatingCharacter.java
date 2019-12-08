char firstNotRepeatingCharacter(String s) {
    int[] charCount = new int[26];
    int[] firstIndex = new int[26];
    
    int N = s.length();
    for (int i = 0; i < N; i++) {
        int charIndex = s.charAt(i) - 'a';
        
        if (charCount[charIndex] == 0) {
            firstIndex[charIndex] = i;
        }
        
        charCount[charIndex]++;
    }
    
    char firstChar = '_';
    int firstCharIndex = Integer.MAX_VALUE;
    for (int i = 0; i < 26; i++) {
        if (charCount[i] == 1) {
            if (firstCharIndex > firstIndex[i]) {
                firstCharIndex = firstIndex[i];
                firstChar = (char) (i + 'a');
            }
        }
    }
    
    return firstChar;
}
