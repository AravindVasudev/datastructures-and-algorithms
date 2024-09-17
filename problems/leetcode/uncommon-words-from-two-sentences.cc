// https://leetcode.com/problems/uncommon-words-from-two-sentences
class Solution {
private:
    template <typename Out>
    static void split(const std::string& s, char delim, Out result) {
        std::istringstream iss(s);
        std::string item;

        while (std::getline(iss, item, delim)) {
            *result++ = item;
        }
    }

    static std::vector<std::string> split(const std::string& s, char delim) {
        std::vector<std::string> elems;
        split(s, delim, std::back_inserter(elems));
        return elems;
    }
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> wordCount;
    
        for (const auto& s : split(s1, ' ')) {
            wordCount[s]++;
        }

        for (const auto& s : split(s2, ' ')) {
            wordCount[s]++;
        }

        vector<std::string> result;
        for (const auto& [string, freq] : wordCount) {
            if (freq == 1) {
                result.push_back(string);
            }
        }

        return result;
    }
};
