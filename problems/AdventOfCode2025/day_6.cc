#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

std::vector<std::string> readInputFile(std::ifstream& input) {
  std::vector<std::string> content;
  std::string line;
  while (std::getline(input, line)) {
    content.push_back(line);
  }

  return content;
}

/**
 * The operation symbols are aligned to the beginning of the equation. This
 * fn identifies all the points of split. Given the numbers are read vertically,
 * the alignment of the digits change the final outcome, hence the necessity
 * of finding the split points.
 */
std::vector<size_t> findSplitPoints(const std::string& operations) {
  std::vector<size_t> splitPoints;
  const auto size = operations.size();

  // Ignore first char given we split from second.
  for (auto i = 1; i < size; i++) {
    if (operations[i] != ' ') {  // Beginning of the next equation.
      splitPoints.push_back(i - 1);
    }
  }

  return splitPoints;
}

std::vector<std::string> splitRow(const std::string& row,
                                  const std::vector<size_t>& splitPoints) {
  std::vector<std::string> parsed;
  const auto size = splitPoints.size();

  for (auto i = 0; i <= size; i++) {
    const auto begin = i == 0 ? 0 : splitPoints[i - 1] + 1;
    const auto length = splitPoints[i] - begin;
    parsed.push_back(row.substr(begin, length));
  }

  return parsed;
}

std::pair<std::vector<std::vector<std::string>>, std::vector<char>>
parseInputFile(std::ifstream& input) {
  const auto content = readInputFile(input);
  const auto size = content.size();

  // Parse operations into chars.
  std::vector<char> operations;
  std::istringstream opStream(content[size - 1]);
  char token;

  while (opStream >> token) {
    operations.push_back(token);
  }

  // Split values with alignment maintained.
  const auto splitPoints = findSplitPoints(content[size - 1]);
  std::vector<std::vector<std::string>> problems;

  // Last line is operations, which is already parsed.
  for (auto row = 0; row < size - 1; row++) {
    problems.push_back(splitRow(content[row], splitPoints));
  }

  return {problems, operations};
}

long part1(const std::vector<std::vector<std::string>>& problems,
           const std::vector<char>& operations) {
  size_t X{problems.size()}, Y{problems[0].size()};
  long result{};

  for (auto j = 0; j < Y; j++) {
    long aggregate = operations[j] == '+' ? 0 : 1;  // identity value.

    for (auto i = 0; i < X; i++) {
      if (operations[j] == '+') {
        aggregate += std::stol(problems[i][j]);
      } else {
        aggregate *= std::stol(problems[i][j]);
      }
    }

    result += aggregate;
  }

  return result;
}

long aggregateCol(const std::vector<std::vector<std::string>>& problems,
                  int col, char op) {
  const auto size = problems.size();
  long aggregate = op == '+' ? 0 : 1;  // identity value.

  for (int digit = 0; true; digit++) {
    std::string num;

    for (size_t row = 0; row < size; row++) {
      auto val = problems[row][col][digit];
      if (val == '\0') {
        continue;
      }

      num += val;
    }

    if (num.empty()) {
      break;
    }

    if (op == '+') {
      aggregate += std::stol(num);
    } else {
      aggregate *= std::stol(num);
    }
  }

  return aggregate;
}

long part2(const std::vector<std::vector<std::string>>& problems,
           const std::vector<char>& operations) {
  size_t X{problems.size()}, Y{problems[0].size()};
  long result{};

  for (auto j = 0; j < Y; j++) {
    result += aggregateCol(problems, j, operations[j]);
  }

  return result;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  auto [problems, operations] = parseInputFile(input);

  std::cout << "Part 1: " << part1(problems, operations) << std::endl;
  std::cout << "Part 2: " << part2(problems, operations) << std::endl;
}