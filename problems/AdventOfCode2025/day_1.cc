#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

const int DIAL_SIZE = 100;
const int DIAL_START = 50;

long mod(long a, long b) {
  return (a % b + b) % b;
}

std::pair<long, long> countZerosIneffient(const std::vector<std::pair<char, long>>& instructions, long position = DIAL_START) {
  std::pair<long, long> result;

  for (const auto& instruction : instructions) {
    for (int i = 0; i < instruction.second; i++) {
      position += instruction.first == 'R' ? 1 : -1;
      position = mod(position, DIAL_SIZE);

      if (position == 0) {
        result.second++;
      }
    }

    if (position == 0) {
      result.first++;
    }
  }

  return result;
}

std::pair<long, long> countZeros(const std::vector<std::pair<char, long>>& instructions, long position = DIAL_START) {
  std::pair<long, long> result;

  for (const auto& instruction : instructions) {
    int rotation = instruction.first == 'R' ? (position + instruction.second) : (position - instruction.second);

    result.second += std::abs(rotation / DIAL_SIZE);
    if (position != 0 && rotation <= 0) {
      result.second++;
    }

    position = mod(rotation, DIAL_SIZE);
    if (position == 0) {
      result.first++;
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
  std::vector<std::pair<char, long>> instructions;
  while (std::getline(input, line)) {
    std::istringstream lineStream(line);
    char direction;
    long distance;

    lineStream >> direction >> distance;
    instructions.push_back({direction, distance});
  }

  const auto result = countZeros(instructions);
  const auto inefficient = countZerosIneffient(instructions);

  std::cout << "Efficient: Part 1 - " << result.first << " Part 2 - " << result.second << std::endl;
  std::cout << "Inefficient: Part 1 - " << inefficient.first << " Part 2 - " << inefficient.second << std::endl;
}
