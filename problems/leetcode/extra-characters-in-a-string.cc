// https://leetcode.com/problems/extra-characters-in-a-string/
class Solution {
private:
    template<typename StringSet, typename StringMap>
    int minExtraChar(const std::string& s, const StringSet& dictionary, StringMap& memo) {
        // If done with the string, no extra char needed.
        if (s.size() == 0) {
            return 0;
        }

        // Check memo if already computed.
        if (const auto& it = memo.find(s); it != memo.end()) {
            return it->second;
        }

        int N = s.size();
        int min = std::numeric_limits<int>::max();
        std::string aggregate;

        for (int i = 0; i < N; i++) {
            aggregate += s[i];
            int curExtraChar = dictionary.contains(aggregate) ? 0 : aggregate.size();
            curExtraChar += minExtraChar(s.substr(i + 1), dictionary, memo);
            min = std::min(min, curExtraChar);
        }

        return memo[s] = min;
    }
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        std::unordered_set<std::string> dict(dictionary.begin(), dictionary.end());
        std::unordered_map<std::string, int> memo;
        return minExtraChar(s, dict, memo);
    }
};
