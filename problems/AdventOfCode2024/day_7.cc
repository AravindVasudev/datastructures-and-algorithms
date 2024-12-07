/*
$ hyperfine --runs 10 ./day_7
Benchmark 1: ./day_7
  Time (mean ± σ):     663.7 ms ±   2.0 ms    [User: 657.6 ms, System: 5.2 ms]
  Range (min … max):   660.8 ms … 666.4 ms    10 runs
*/

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

std::pair<long long, std::vector<long long>> parseEquation(
    const std::string& equation) {
  std::istringstream ss(equation);
  std::string line;

  // Parse rhs.
  getline(ss, line, ':');
  long rhs = std::stol(line);
  getline(ss, line, ' ');

  // Parse lhs.
  std::vector<long long> lhs;
  while (getline(ss, line, ' ')) {
    lhs.push_back(std::stol(line));
  }

  return {rhs, lhs};
}

bool isSolvable(const std::pair<long long, std::vector<long long>>& equation,
                size_t i = 0, long long total = 0) {
  if (i == equation.second.size()) {
    return total == equation.first;
  }

  return isSolvable(equation, i + 1, total + equation.second[i]) ||
         isSolvable(equation, i + 1, total * equation.second[i]);
}

long long concat(const long long num1, const long long num2) {
  return std::stol(std::to_string(num1) + std::to_string(num2));
}

bool isSolvableWithConcat(
    const std::pair<long long, std::vector<long long>>& equation,
    const size_t i = 0, const long long total = 0) {
  if (i == equation.second.size()) {
    return total == equation.first;
  }

  return isSolvableWithConcat(equation, i + 1, total + equation.second[i]) ||
         isSolvableWithConcat(equation, i + 1, total * equation.second[i]) ||
         isSolvableWithConcat(equation, i + 1,
                              concat(total, equation.second[i]));
}

long long part1(const std::vector<std::pair<long long, std::vector<long long>>>&
                    equations) {
  long long result{};
  for (const auto& equation : equations) {
    if (isSolvable(equation)) {
      result += equation.first;
    }
  }

  return result;
}

long long part2(const std::vector<std::pair<long long, std::vector<long long>>>&
                    equations) {
  long long result{};
  for (const auto& equation : equations) {
    if (isSolvableWithConcat(equation)) {
      result += equation.first;
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

  std::vector<std::pair<long long, std::vector<long long>>> equations;
  std::string line;

  while (getline(input, line)) {
    equations.emplace_back(parseEquation(line));
  }

  input.close();

  std::cout << "Part 1: " << part1(equations) << std::endl;
  std::cout << "Part 2: " << part2(equations) << std::endl;
}
