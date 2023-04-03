// https://leetcode.com/problems/richest-customer-wealth/
use std::cmp;

impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut max = 0;
        for account in &accounts {
            max = cmp::max(max, account.iter().sum());
        }

        max
    }
}
