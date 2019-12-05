public class Solution {
    public ArrayList<Integer> plusOne(ArrayList<Integer> A) {
        if (A == null || A.size() == 0) {
            return new ArrayList<Integer>();
        }
        
        if (A.get(0) != 0) A.add(0, 0);
        int carry = 1;
        for (int i = A.size() - 1; i >= 0; i--) {
            int newVal = A.get(i) + carry;
            if (newVal > 9) {
                newVal = newVal % 10;
                carry = 1;
            } else {
                carry = 0;
            }
            
            A.set(i, newVal);
        }
        
        while (A.get(0) == 0) A.remove(0);
        
        return A;
    }
}
