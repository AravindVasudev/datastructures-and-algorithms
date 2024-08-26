// https://leetcode.com/problems/count-and-say/
class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) {
            return "1";
        }

        return rle(countAndSay(n - 1));
    }

private:
    std::string rle(const std::string& str) {
        if (str.size() == 0) {
            throw std::runtime_error("RLE requires string.size() > 0");
        }

        std::stringstream encoded;
        char prev = str[0];
        int runLength = 0;

        for (const auto& c : str) {
            if (c == prev) {
                runLength++;
                continue;
            }

            encoded << runLength << prev;
            prev = c;
            runLength = 1;
        }

        encoded << runLength << prev;
        return encoded.str();
    }
};
