#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

long part1(const std::vector<std::pair<int, int>>& redTiles) {
  long result{};
  const auto size = redTiles.size();

  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      long l = abs(redTiles[i].first - redTiles[j].first) + 1;
      long w = abs(redTiles[i].second - redTiles[j].second) + 1;

      result = std::max(result, l * w);
    }
  }

  return result;
}

int main() {
  // Read input file.
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::vector<std::pair<int, int>> redTiles;
  std::string line;
  while (std::getline(input, line)) {
    std::istringstream iss(line);
    std::string token;
    std::pair<int, int> tile;

    std::getline(iss, token, ',');
    tile.first = std::stol(token);

    std::getline(iss, token);
    tile.second = std::stol(token);

    redTiles.push_back(tile);
  }

  std::cout << "Part 1: " << part1(redTiles) << std::endl;
  std::cout << "Part 2: " << "b" << std::endl;
}