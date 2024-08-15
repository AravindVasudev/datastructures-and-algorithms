// https://leetcode.com/problems/lemonade-change/
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fives = 0, tens = 0;
        for (auto bill : bills) {
            switch (bill) {
                case 5:
                    fives++;
                    break;
                case 10:
                    if (fives <= 0) {
                        return false;
                    }

                    tens++;
                    fives--;
                    break;
                case 20:
                    if (fives <= 0 || !(fives > 2 || tens > 0)) {
                        return false;
                    }

                    if (tens > 0) {
                        tens--;
                        fives--;
                    } else {
                        fives -= 3;
                    }
                    break;
            }
        }

        return true;
    }
};
