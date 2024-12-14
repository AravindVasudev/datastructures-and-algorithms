#include <cmath>
#include <format>
#include <fstream>
#include <iostream>
#include <limits>
#include <regex>

std::regex Pattern("p=([-]?\\d+),([-]?\\d+) v=([-]?\\d+),([-]?\\d+)");
const int X = 101, Y = 103;  // Grid Dimensions.
const int leftX = static_cast<int>(floor(X / 2.0));
const int rightX = static_cast<int>(ceil(X / 2.0));
const int leftY = static_cast<int>(floor(Y / 2.0));
const int rightY = static_cast<int>(ceil(Y / 2.0));

struct Robot {
  std::pair<int, int> position, velocity;

  void move(int seconds) {
    position.first = (position.first + velocity.first * seconds) % X;
    if (position.first < 0) {
      position.first += X;  // Wrap.
    }

    position.second = (position.second + velocity.second * seconds) % Y;
    if (position.second < 0) {
      position.second += Y;  // Wrap.
    }
  }

  static void move(std::vector<Robot>& robots, int seconds) {
    for (auto& robot : robots) {
      robot.move(seconds);
    }
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

void visualize(const std::vector<Robot>& robots, std::ostream& out) {
  std::vector<std::vector<int>> grid(Y, std::vector<int>(X, 0));

  // Place robots on the grid.
  for (const auto& robot : robots) {
    grid[robot.position.second][robot.position.first]++;
  }

  // Print.
  for (const auto& row : grid) {
    for (const auto col : row) {
      out << (col ? '*' : '.');
    }
    out << std::endl;
  }
}

int safetyFactor(const std::vector<Robot>& robots) {
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

int part1(std::vector<Robot> robots, const int seconds = 100) {
  Robot::move(robots, seconds);
  return safetyFactor(robots);
}

void writeState(const std::vector<Robot>& robots, std::string filename) {
  std::ofstream file(filename);
  if (!file.is_open()) {
    std::cerr << "Cannot open " << filename << std::endl;
    return;
  }

  visualize(robots, file);
  file.close();
}

void part2(std::vector<Robot> robots, int frames = 10000) {
  int maxSF = std::numeric_limits<int>::max();

  for (int second = 0; second < frames; second++) {
    Robot::move(robots, 1);
    int curSF = safetyFactor(robots);
    if (curSF < maxSF) {
      maxSF = curSF;
      writeState(robots, std::format("{}.txt", second + 1));
    }
  }
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

  std::cout << "Part 1: " << part1(robots) << std::endl;
  part2(robots);
}
