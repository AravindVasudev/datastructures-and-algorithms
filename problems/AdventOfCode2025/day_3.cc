#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

struct PairComparator {
  bool operator()(const std::pair<int, int>& a,
                  const std::pair<int, int>& b) const {
    if (a.first != b.first) {
      return a.first < b.first; // Descending by value.
    }

    return a.second > b.second; // Ascending by index.
  }
};

inline long ctol(const char c) { return c - '0'; }

long findMax(const std::string& bank, int length) {
  const auto size = bank.size();
  if (size <= length) {
    return std::stol(bank);
  }

  // We need to pick max from (size - length) and repeat until all the length
  // digits are picked.
  std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                      PairComparator>
      window;
  auto windowSize = size - length;
  for (auto i = 0; i < windowSize; i++) {
    window.push({ctol(bank[i]), i});
  }

  std::string max;
  int prevIndex = -1;
  for (auto i = windowSize; i < size; i++) {
    // Add next digit.
    window.push({ctol(bank[i]), i});

    // clear values from before the previous picked index.
    while (prevIndex > window.top().second) {
      window.pop();
    }

    // Find the largest next digit.
    auto [val, index] = window.top();

    max += std::to_string(val);
    prevIndex = index;
    window.pop();
  }

  return std::stol(max);
}

long findMaxJoltageSum(const std::vector<std::string>& banks, int length) {
  long result{};
  for (const auto& bank : banks) {
    result += findMax(bank, length);
  }

  return result;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::string line;
  std::vector<std::string> banks;
  while (std::getline(input, line)) {
    banks.push_back(line);
  }

  std::cout << "Part 1: " << findMaxJoltageSum(banks, 2) << std::endl;
  std::cout << "Part 2: " << findMaxJoltageSum(banks, 12) << std::endl;
}