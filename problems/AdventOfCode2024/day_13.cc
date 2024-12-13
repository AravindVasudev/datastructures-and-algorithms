#include <algorithm>
#include <format>
#include <fstream>
#include <iostream>
#include <limits>
#include <regex>

const std::regex ButtonPattern("X\\+([0-9]{1,}), Y\\+([0-9]{1,})");
const std::regex PricePattern("X=([0-9]{1,}), Y=([0-9]{1,})");

struct ClawMachine {
  std::pair<long, long> buttonA, buttonB, price;
};

ClawMachine parse(const std::string& buttonA, const std::string& buttonB,
                  const std::string& price) {
  std::smatch match;
  ClawMachine machine;

  // We expect input to be formatted, hence no validation.
  // Parse button A.
  std::regex_search(buttonA, match, ButtonPattern);
  machine.buttonA.first = std::stoi(match[1].str());
  machine.buttonA.second = std::stoi(match[2].str());

  // Parse button B.
  std::regex_search(buttonB, match, ButtonPattern);
  machine.buttonB.first = std::stoi(match[1].str());
  machine.buttonB.second = std::stoi(match[2].str());

  // Parse result
  // Parse button A.
  std::regex_search(price, match, PricePattern);
  machine.price.first = std::stoi(match[1].str());
  machine.price.second = std::stoi(match[2].str());

  return machine;
}

long play(const ClawMachine& machine, long priceX, long priceY,
          std::unordered_map<std::string, long>& memo) {
  if (priceX == 0 && priceY == 0) {
    return 0;  // We got the price baby!
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

long playAll(const std::vector<ClawMachine>& machines, long offset = 0) {
  long total{};
  for (const auto& machine : machines) {
    std::unordered_map<std::string, long> memo;
    if (auto tokens = play(machine, machine.price.first + offset,
                           machine.price.second + offset, memo);
        tokens > 0) {
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
    std::getline(file, buttonA);  // Skip empty line.
  }

  std::cout << "Part 1: " << playAll(machines) << std::endl;
  // std::cout << "Part 2: " << playAll(machines, 10000000000000) << std::endl;
}
