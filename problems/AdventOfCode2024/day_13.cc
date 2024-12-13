#include <algorithm>
#include <format>
#include <fstream>
#include <iostream>
#include <limits>
#include <regex>

const std::regex Pattern("X[\\+=](\\d+), Y[\\+=](\\d+)");

struct ClawMachine {
  std::pair<long, long> buttonA, buttonB, price;
};

ClawMachine parse(const std::string &buttonA, const std::string &buttonB,
                  const std::string &price) {
  std::smatch match;
  ClawMachine machine;

  // We expect input to be formatted, hence no validation.
  // Parse button A.
  std::regex_search(buttonA, match, Pattern);
  machine.buttonA.first = std::stoi(match[1].str());
  machine.buttonA.second = std::stoi(match[2].str());

  // Parse button B.
  std::regex_search(buttonB, match, Pattern);
  machine.buttonB.first = std::stoi(match[1].str());
  machine.buttonB.second = std::stoi(match[2].str());

  // Parse result
  std::regex_search(price, match, Pattern);
  machine.price.first = std::stoi(match[1].str());
  machine.price.second = std::stoi(match[2].str());

  return machine;
}

long play(const ClawMachine &machine, long priceX, long priceY,
          std::unordered_map<std::string, long> &memo) {
  if (priceX == 0 && priceY == 0) {
    return 0; // We got the price baby!
  }

  if (priceX < 0 || priceY < 0) {
    return -1;
  }

  auto key = std::format("{},{}", priceX, priceY);
  if (memo.find(key) != memo.cend()) {
    return memo[key];
  }

  auto playA = play(machine, priceX - machine.buttonA.first,
                    priceY - machine.buttonA.second, memo);
  auto playB = play(machine, priceX - machine.buttonB.first,
                    priceY - machine.buttonB.second, memo);

  if (playA < 0 && playB < 0) {
    return memo[key] = -1;
  } else if (playA < 0) {
    return memo[key] = 1 + playB;
  } else if (playB < 0) {
    return memo[key] = 3 + playA;
  }

  return memo[key] = std::min(3 + playA, 1 + playB);
}

// Inefficient: Dynamic Programming Attempt.
long playAllInefficient(const std::vector<ClawMachine> &machines,
                        long offset = 0) {
  long total{};
  for (const auto &machine : machines) {
    std::unordered_map<std::string, long> memo;
    if (auto tokens = play(machine, machine.price.first + offset,
                           machine.price.second + offset, memo);
        tokens > 0) {
      total += tokens;
    }
  }

  return total;
}

double computeA(long x1, long y1, long x2, long y2, long z1, long z2) {
  const double numerator = (y2 * z1) - (y1 * z2);
  const double denominator = (y2 * x1) - (y1 * x2);

  return numerator / denominator;
}

double computeB(long x1, long y1, long z1, double a) {
  return (z1 - x1 * a) / static_cast<double>(y1);
}

long solve(const ClawMachine &machine) {
  /*
   * ik this can probably be solved using the matrix method much simpler.
   * However, I don't wanna throw in a whole 3rd party math lib or write my
   * own matrix ops. Hence, I'm falling back to the simple substitution method.
   * x1*a + y1*b = z1
   * x2*a + y2*b = z2
   *
   * b = (z1 - x1*a) / y1
   * b = (z2 - x2*a) / y2
   * y2 * (z1 - x1*a) = y1 * (z2 - x2*a)
   * y2*z1 - y2*x1*a = y1*z2 - y1*x2*a
   * y2*z1 - y1*z2 = y2*x1*a - y1*x2*a
   * y2*z1 - y1*z2 = (y2*x1 - y1*x2) * a
   * a = (y2*z1 - y1*z2) / (y2*x1 - y1*x2)
   * b = (z1 - x1*a) / y1 (copied from above).
   *
   * The above equations assume there is a solution. There could be no solutions
   * when either the line is parallel, or the same, or maybe there is no whole
   * number solution.
   */

  // Intentionally truncate the decimal part. We only care about whole number
  // solutions.
  long a = computeA(machine.buttonA.first, machine.buttonB.first,
                    machine.buttonA.second, machine.buttonB.second,
                    machine.price.first, machine.price.second);
  long b = computeB(machine.buttonA.first, machine.buttonB.first,
                    machine.price.first, a);

  auto lhs1 = machine.buttonA.first * a + machine.buttonB.first * b;
  auto lhs2 = machine.buttonA.second * a + machine.buttonB.second * b;

  if (lhs1 != machine.price.first || lhs2 != machine.price.second) {
    return -1; // No solution.
  }

  return 3 * a + b;
}

// Efficient: System of linear equations.
long playAll(std::vector<ClawMachine> &machines, long offset = 0) {
  long total{};
  for (auto &machine : machines) {
    std::unordered_map<std::string, long> memo;

    // Mutating the original machine to save time.
    machine.price.first += offset;
    machine.price.second += offset;
    if (auto tokens = solve(machine); tokens > 0) {
      total += tokens;
    }
  }

  return total;
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Cannot open input.txt" << std::endl;
    return 1;
  }

  std::vector<ClawMachine> machines;
  std::string buttonA, buttonB, price;

  while (std::getline(file, buttonA)) {
    std::getline(file, buttonB);
    std::getline(file, price);

    machines.emplace_back(parse(buttonA, buttonB, price));
    std::getline(file, buttonA); // Skip empty line.
  }

  // std::cout << "Part 1: " << playAllInefficient(machines) << std::endl;
  std::cout << "Part 1: " << playAll(machines) << std::endl;
  std::cout << "Part 2: " << playAll(machines, 10000000000000) << std::endl;
}
