#include <cmath>
#include <fstream>
#include <iostream>
#include <regex>

std::regex Pattern("p=([-]?\\d+),([-]?\\d+) v=([-]?\\d+),([-]?\\d+)");
const int X = 101, Y = 103;  // Grid Dimensions.
const int leftX = static_cast<int>(floor(X / 2.0));
const int rightX = static_cast<int>(ceil(X / 2.0));
const int leftY = static_cast<int>(floor(Y / 2.0));
const int rightY = static_cast<int>(ceil(Y / 2.0));

struct Robot {
  std::pair<int, int> position, velocity;

  void update() {
    position.first = wrap(position.first + velocity.first, X);
    position.second = wrap(position.second + velocity.second, Y);
  }

  static int wrap(int i, int N) {
    if (i < 0) {
      return N + (i % N);
    }

    return (i % N);
  }
};

Robot parse(const std::string& line) {
  Robot robot;
  std::smatch matches;
  std::regex_search(line, matches, Pattern);

  robot.position.first = std::stoi(matches[1]);
  robot.position.second = std::stoi(matches[2]);
  robot.velocity.first = std::stoi(matches[3]);
  robot.velocity.second = std::stoi(matches[4]);

  return robot;
}

// debugging helper.
void visualize(const std::vector<Robot>& robots) {
  std::vector<std::vector<int>> grid(Y, std::vector<int>(X, 0));

  // Place robots on the grid.
  for (const auto& robot : robots) {
    grid[robot.position.second][robot.position.first]++;
  }

  // Print.
  std::cout << std::endl;
  for (const auto& row : grid) {
    for (const auto col : row) {
      if (col == 0) {
        std::cout << '.';
      } else {
        std::cout << col;
      }
    }

    std::cout << std::endl;
  }
}

int safetyFactor(std::vector<Robot>& robots, int seconds = 100) {
  // Simulate robot moving for the given seconds.
  while (seconds--) {
    for (auto& robot : robots) {
      robot.update();
    }
  }

  // visualize(robots);

  // Compute safety factor.
  std::array<int, 4> quadrants = {0};
  for (const auto& robot : robots) {
    if (0 <= robot.position.first &&
        robot.position.first < leftX) {  // Left half.
      if (0 <= robot.position.second &&
          robot.position.second < leftY) {  // Top half.
        quadrants[0]++;
      } else if (rightY <= robot.position.second) {  // Bottom half.
        quadrants[2]++;
      }
    } else if (rightX <= robot.position.first) {  // Right half.
      if (0 <= robot.position.second &&
          robot.position.second < leftY) {  // Top half.
        quadrants[1]++;
      } else if (rightY <= robot.position.second) {  // Bottom half.
        quadrants[3]++;
      }
    }
  }

  return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3];
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Cannot open input.txt" << std::endl;
    return 1;
  }

  std::vector<Robot> robots;
  std::string line;

  while (std::getline(file, line)) {
    robots.emplace_back(parse(line));
  }

  std::cout << "Part 1: " << safetyFactor(robots) << std::endl;
}
