#include <algorithm>
#include <format>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_set>

std::unordered_set<std::string> split(std::string str, char delimiter) {
  std::unordered_set<std::string> result;
  std::istringstream ss(str);
  std::string token;

  while (std::getline(ss, token, delimiter)) {
    size_t start = token.find_first_not_of(' ');
    size_t end = token.find_last_not_of(' ');
    if (start != std::string::npos && end != std::string::npos) {
      token = token.substr(start, end - start + 1);
    }
    result.insert(token);
  }

  return result;
}

long canForm(std::string pattern, const std::unordered_set<std::string>& towels,
             std::vector<long>& memo, size_t p = 0) {
  const size_t N = pattern.size();
  if (p == N) {
    return 1;
  }

  if (memo[p] != -1) {
    return memo[p];
  }

  std::string accumlator;
  long result{};
  for (size_t i = p; i < N; i++) {
    accumlator += pattern[i];
    if (towels.find(accumlator) != towels.cend()) {
      if (long r = canForm(pattern, towels, memo, i + 1); r > 0) {
        result += r;
      }
    }
  }

  return memo[p] = result > 0 ? result : -1;
}

std::pair<long, long> formations(const std::vector<std::string>& patterns,
          const std::unordered_set<std::string>& towels) {
  std::pair<long, long> result{};
  for (const auto& pattern : patterns) {
    std::vector<long> memo(pattern.size(), -1);
    if (long r = canForm(pattern, towels, memo); r > 0) {
      result.first++;
      result.second += r;
    }
  }

  return result;
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Unable to open input.txt" << std::endl;
    return 1;
  }

  // Parse input file.
  std::string line;
  std::getline(file, line);
  auto towels = split(line, ',');
  std::getline(file, line);  // Empty line

  std::vector<std::string> patterns;
  while (std::getline(file, line)) {
    patterns.push_back(line);
  }

  auto result = formations(patterns, towels);
  std::cout << "Part 1: " << result.first << std::endl;
  std::cout << "Part 1: " << result.second << std::endl;
}
