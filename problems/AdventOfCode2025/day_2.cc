#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_set>

std::pair<long, long> splitRange(const std::string& range) {
  const size_t delimiter = range.find('-');
  return {std::stol(range.substr(0, delimiter)),
          std::stol(range.substr(delimiter + 1))};
}

std::vector<std::pair<long, long>> parseInput(const std::string& input) {
  std::vector<std::pair<long, long>> parsed;
  std::stringstream stream(input);

  std::string range;
  while(std::getline(stream, range, ',')) {
    parsed.push_back(splitRange(range));
  }

  return parsed;
}

bool isValidPart1(const std::string& productId) {
  // Odd length can't repeat twice.
  const size_t size = productId.size();
  if (size % 2 == 1) {
    return true;
  }

  // Pattern should repeat from the middle.
  const size_t mid = size / 2;
  for (size_t i = 0; i < mid; i++) {
    if (productId[i] != productId[i + mid]) {
      return true;
    }
  }
  
  return false;
}

long mod(long a, long b) {
  return (a % b + b) % b;
}

bool isEntireStringRepeating(const std::string& productId, const size_t end) {
  size_t nextIndex{};
  for (size_t i = end; i < productId.size(); i++) {
    if (productId[i] != productId[nextIndex])  {
      return false;
    }

    // Move nextIndex, wrap around if outside the current window.
    nextIndex = mod(nextIndex + 1, end);
  }

  return true;
}

bool isValidPart2(const std::string& productId) {
  // (size - end) because we at least need that many more chars to at least
  // have one full repeat of the current window.
  const size_t size = productId.size();
  for (size_t end = 1; end <= (size - end); end++) {
    // The current window size cannot wrap around the entire string so skip
    // the check.
    if (size % end != 0) {
      continue;
    }

    // Check if productId[start:end) covers the entire string.
    if (isEntireStringRepeating(productId, end)) {
      return false;
    }
  }

  return true;
}

std::pair<long, long> countInvalids(const std::vector<std::pair<long, long>>& ranges) {
  std::pair<long, long> result;
  for (const auto& range : ranges) {
    for (long i = range.first; i <= range.second; i++) {
      const std::string productId = std::to_string(i);
      if (!isValidPart1(productId)) {
        result.first += i;
      }

      if (!isValidPart2(productId)) {
        result.second += i;
      }
    }
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
  std::getline(input, line);
  auto ranges = parseInput(line);

  const auto result = countInvalids(ranges);
  std::cout << "Part 1: " << result.first << std::endl;
  std::cout << "Part 2: " << result.second << std::endl;
}