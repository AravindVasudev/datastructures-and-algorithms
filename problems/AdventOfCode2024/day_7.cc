/*
* Instructions for Apple Silicon (M1 Pro):

```
$ brew install folly
$ g++ -std=c++20 -I /opt/homebrew/Cellar/folly/2024.12.02.00/include -I
/opt/homebrew/Cellar/boost/1.86.0/include -I
/opt/homebrew/Cellar/glog/0.6.0/include -I
/opt/homebrew/Cellar/gflags/2.2.2/include -I
/opt/homebrew/Cellar/double-conversion/3.3.0/include -I
/opt/homebrew/Cellar/fmt/11.0.2/include -I
/opt/homebrew/Cellar/libevent/2.1.12_1/include -L
/opt/homebrew/Cellar/folly/2024.12.02.00/lib -L
/opt/homebrew/Cellar/boost/1.86.0/lib -L /opt/homebrew/Cellar/glog/0.6.0/lib -L
/opt/homebrew/Cellar/gflags/2.2.2/lib -L
/opt/homebrew/Cellar/double-conversion/3.3.0/lib -L
/opt/homebrew/Cellar/fmt/11.0.2/lib -L
/opt/homebrew/Cellar/libevent/2.1.12_1/lib -lfolly -lglog -O3 day_7.cc -o day_7
$ ./day_7
Part 1: 8401132154762
Part 2: 95297119227552

$ hyperfine --runs 10 ./day_7
Benchmark 1: ./day_7
  Time (mean ± σ):      18.0 ms ±   1.1 ms    [User: 60.7 ms, System: 4.1 ms]
  Range (min … max):    16.9 ms …  20.8 ms    10 runs
```

*/

#include <folly/executors/CPUThreadPoolExecutor.h>
#include <folly/futures/Future.h>

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

std::pair<long, std::vector<long>> parseEquation(const std::string& equation) {
  std::istringstream ss(equation);
  std::string line;

  // Parse rhs.
  getline(ss, line, ':');
  long rhs = std::stol(line);
  getline(ss, line, ' ');

  // Parse lhs.
  std::vector<long> lhs;
  while (getline(ss, line, ' ')) {
    lhs.push_back(std::stol(line));
  }

  return {rhs, lhs};
}

bool isSolvable(const std::pair<long, std::vector<long>>& equation,
                const size_t i = 0, const long total = 0) {
  if (i == equation.second.size()) {
    return total == equation.first;
  }

  if (total > equation.first) {
    return false;  // branch pruning.
  }

  return isSolvable(equation, i + 1, total + equation.second[i]) ||
         isSolvable(equation, i + 1, total * equation.second[i]);
}

long concat(const long num1, const long num2) {
  // return std::stol(std::to_string(num1) + std::to_string(num2));
  long pow = 10;
  while (num2 >= pow) {
    pow *= 10;
  }

  return num1 * pow + num2;
}

bool isSolvableWithConcat(const std::pair<long, std::vector<long>>& equation,
                          const size_t i = 0, const long total = 0) {
  if (i == equation.second.size()) {
    return total == equation.first;
  }

  if (total > equation.first) {
    return false;  // branch pruning.
  }

  return isSolvableWithConcat(equation, i + 1, total + equation.second[i]) ||
         isSolvableWithConcat(equation, i + 1, total * equation.second[i]) ||
         isSolvableWithConcat(equation, i + 1,
                              concat(total, equation.second[i]));
}

long part1(const std::vector<std::pair<long, std::vector<long>>>& equations) {
  const int N = equations.size();
  long total{};

  const auto numCores = std::thread::hardware_concurrency();
  folly::CPUThreadPoolExecutor executor(numCores);
  std::vector<folly::Future<std::pair<bool, size_t>>> futures;

  for (int i = 0; i < N; i++) {
    futures.push_back(folly::via(&executor, [&equations, i]() {
      return std::make_pair(isSolvable(equations[i]), i);
    }));
  }

  auto results = folly::collectAll(futures).get();  // wait.
  for (const auto& r : results) {
    auto res = r.value();
    if (res.first) {
      total += equations[res.second].first;
    }
  }

  return total;
}

long part2(const std::vector<std::pair<long, std::vector<long>>>& equations) {
  const int N = equations.size();
  long total{};

  const auto numCores = std::thread::hardware_concurrency();
  folly::CPUThreadPoolExecutor executor(numCores);
  std::vector<folly::Future<std::pair<bool, size_t>>> futures;

  for (int i = 0; i < N; i++) {
    futures.push_back(folly::via(&executor, [&equations, i]() {
      return std::make_pair(isSolvableWithConcat(equations[i]), i);
    }));
  }

  auto results = folly::collectAll(futures).get();  // wait.
  for (const auto& r : results) {
    auto res = r.value();
    if (res.first) {
      total += equations[res.second].first;
    }
  }

  return total;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::pair<long, std::vector<long>>> equations;
  std::string line;

  while (getline(input, line)) {
    equations.emplace_back(parseEquation(line));
  }

  input.close();

  std::cout << "Part 1: " << part1(equations) << std::endl;
  std::cout << "Part 2: " << part2(equations) << std::endl;
}
