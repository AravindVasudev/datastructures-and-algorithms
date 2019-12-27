class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
                continue;
            }
            
            if (stack.empty()) {
                return false;
            }
            
            char top = stack.pop();
            if (!((c == ')' && top == '(') || (c == '}' && top == '{') || (c == ']' && top == '['))) {
                return false;
            }
        }
        
        return stack.empty();
    }
}