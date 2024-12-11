#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>

std::vector<long> parse(const std::string str) {
  std::stringstream ss(str);
  std::string line;
  std::vector<long> result;

  while (ss >> line) {
    result.push_back(std::stol(line));
  }

  return result;
}

inline long hash(long stone, int depth) { return stone * 100 + depth; }

long blink(const long stone, std::unordered_map<long, long>& memo,
           const int depth = 25) {
  if (depth == 0) {  // Done.
    return 1;
  }

  // Cache hit.
  auto key = hash(stone, depth);
  if (memo.find(key) != memo.cend()) {
    return memo[key];
  }

  if (stone == 0) {  // Case '0': flip to '1'.
    return memo[key] = blink(1, memo, depth - 1);
  }

  long digits = static_cast<long>(log10(stone)) + 1;
  if (digits & 1) {  // Case odd: Multiply by 2024.
    return memo[key] = blink(stone * 2024, memo, depth - 1);
  }

  // Case even: Split the number into two halves.
  const long divisor = static_cast<long>(std::pow(10, digits / 2));
  return memo[key] = blink(stone / divisor, memo, depth - 1) +
                     blink(stone % divisor, memo, depth - 1);
}

long countStones(const std::vector<long>& stones, const int blinks) {
  long count{};
  std::unordered_map<long, long> memo;
  for (auto stone : stones) {
    count += blink(stone, memo, blinks);
  }

  return count;
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::string input;
  std::getline(file, input);
  file.close();

  auto stones = parse(input);
  std::cout << "Part 1: " << countStones(stones, 25) << std::endl;
  std::cout << "Part 2: " << countStones(stones, 75) << std::endl;
}
