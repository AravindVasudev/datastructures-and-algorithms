#include <iostream>
#include <map>

std::pair<char, int> longest_consecutive_character(const std::string& str) {
    if (!str.length()) {
        return std::pair<char, int>(' ', -1);
    }

    char max_char, prev_char = 0;
    int count = 0, max_count = 0;

    for (const char& cur : str) {
        if (cur == prev_char) {
            count++;
        } else {
            count = 1;
        }

        if (max_count < count) {
            max_count = count;
            max_char = cur;
        }

        prev_char = cur;
    }

    return std::pair<char, int>(max_char, max_count);
}

int main() {
    std::string str;

    std::cin >> str;

    std::pair<char, int> consecutive_char = longest_consecutive_character(str);

    std::cout
        << consecutive_char.first
        << " : "
        << consecutive_char.second
        << std::endl;

    return 0;
}
