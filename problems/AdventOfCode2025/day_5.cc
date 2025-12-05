#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

std::pair<long, long> splitRange(const std::string& range) {
  const size_t delimiter = range.find('-');
  return {std::stol(range.substr(0, delimiter)),
          std::stol(range.substr(delimiter + 1))};
}

// Parse the range blocks.
std::vector<std::pair<long, long>> parseFreshRange(std::ifstream& file) {
  std::string line;
  std::vector<std::pair<long, long>> freshRanges;

  while (std::getline(file, line)) {
    // Only read first block.
    if (line.empty()) {
      break;
    }

    freshRanges.push_back(splitRange(line));
  }

  return freshRanges;
}

std::vector<long> parseInventory(std::ifstream& file) {
  std::string line;
  std::vector<long> inventory;

  while (std::getline(file, line)) {
    inventory.push_back(std::stol(line));
  }

  return inventory;
}

long countAvailable(const std::vector<std::pair<long, long>>& freshRanges,
                const std::vector<long>& inventory) {
  long count{};

  for (const auto ingredient : inventory) {
    for (const auto& range : freshRanges) {
      if (ingredient >= range.first && ingredient <= range.second) {
        count++;
        break;
      }
    }
  }

  return count;
}

bool doesOverlap(std::pair<long, long> range1, std::pair<long, long> range2) {
  bool isRange1BetweenRange2 = range1.second >= range2.first && range1.second <= range2.second;
  bool isRange2BetweenRange1 = range2.second >= range1.first && range2.second <= range1.second;

  return isRange1BetweenRange2 || isRange2BetweenRange1;
}

std::pair<long, long> mergeRanges(std::pair<long, long> range1, std::pair<long, long> range2) {
  return {std::min(range1.first, range2.first), std::max(range1.second, range2.second)};
}

std::vector<std::pair<long, long>> mergeRanges(std::vector<std::pair<long, long>>& freshRanges) {
  std::sort(freshRanges.begin(), freshRanges.end());

  std::vector<std::pair<long, long>> merged;
  size_t size{freshRanges.size()};
  
  for (size_t i = 0; i < size; i++) {
    auto range = freshRanges[i];
    while (i + 1 < size && doesOverlap(range, freshRanges[i + 1])) {
      range = mergeRanges(range, freshRanges[i + 1]);
      i++;
    }

    merged.push_back(range);
  }


  return merged;
}

long countFresh(std::vector<std::pair<long, long>>& freshRanges) {
  long count{};
  for (const auto& range : mergeRanges(freshRanges)) {
    count += range.second - range.first + 1;
  }

  return count;
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  auto freshRanges = parseFreshRange(input);
  auto inventory = parseInventory(input);

  std::cout << "Part 1: " << countAvailable(freshRanges, inventory) << std::endl;
  std::cout << "Part 2: " << countFresh(freshRanges) << std::endl;
}