// https://leetcode.com/problems/shuffle-string/
impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        let mut shuffled: Vec<char> = vec![' '; s.len()];
        let chars: Vec<char> = s.chars().collect();

        for (i, idx) in indices.iter().enumerate() {
            shuffled[*idx as usize] = chars[i];
        }
        
        return shuffled.iter().collect();
    }
}
