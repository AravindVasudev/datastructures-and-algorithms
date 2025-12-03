#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

inline long ctol(const char c) {
  return c - '0';
}

// long findMax(const std::string& bank, size_t index = 0) {
//   if (index == bank.size()) {
//     return -1;
//   }


// }

long part1(const std::vector<std::string>& banks) {
  long result{};
  for (const auto& bank : banks) {
    const auto size = bank.size();
    long max = 0;
    for (auto i = 0; i < size; i++) {
      for (auto j = i + 1; j < size; j++) {
        max = std::max(max, ctol(bank[i]) * 10 + ctol(bank[j]));
      }
    }

    result += max;
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

  for (auto& bank : banks) {
    std::cout << bank << std::endl;
  }

  std::cout << "Part 1: " << part1(banks) << std::endl;
  std::cout << "Part 2: " << "b" << std::endl;
}