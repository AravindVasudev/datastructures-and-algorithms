// https://leetcode.com/problems/baseball-game/
class Solution {
    public int calPoints(String[] ops) {
        int[] stack = new int[ops.length];
        int top = 0;
        
        for (String operation : ops) {
            switch (operation) {
                case "+":
                    int currentScore = 0;
                    if (top >= 1) {
                        currentScore = stack[top - 1];
                    }
                    
                    if (top >= 2) {
                        currentScore += stack[top - 2];
                    }
                    
                    stack[top++] = currentScore;
                    break;
                case "D":
                    if (top >= 1) {
                        stack[top] = 2 * stack[top - 1];
                        top++;
                    }
                    break;
                case "C":
                    top--;
                    break;
                default:
                    stack[top++] = Integer.parseInt(operation);
            }
        }
        
        int sum = 0;
        for (int i = 0; i < top; i++) {
            sum += stack[i];
        }
        
        return sum;
    }
}
