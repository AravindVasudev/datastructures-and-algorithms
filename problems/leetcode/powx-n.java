// https://leetcode.com/problems/powx-n/
class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        return myPowHelper(x, n);
    }
    
    private double myPowHelper(double x, int n) {
        if (n == 0) {
            return 1;
        }
        
        double half = myPowHelper(x, n / 2);
        double xPowerN = 1;
        if (n % 2 != 0) {
            xPowerN = x;
        }
        
        xPowerN *= half * half;
        return xPowerN;
    }
};
