#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>

enum Opcode {
  ADV = 0,  // A = A % 2^combo(op).
  BXL,      // B = B xor op.
  BST,      // B = combo(op) mod 8.
  JNZ,      // Jump.
  BXC,      // B xor C.
  OUT,      // OUTPUT = combo(op) mod 8.
  BDV,      // B = A % 2^combo(op).
  CDV,      // C = A % 2^combo(op).
};

using Register = int;
Register A, B, C;

inline std::string splitInput(const std::string& input) {
  return input.substr(input.find(": ") + 1);
}

std::vector<int> parseProgram(const std::string& input) {
  std::vector<int> program;
  std::istringstream ss(input);
  std::string line;

  while (std::getline(ss, line, ',')) {
    program.emplace_back(std::stoi(line));
  }

  return program;
}

inline int combo(int operand) {
  if (operand < 4) {
    return operand;
  }

  switch (operand) {
    case 4:
      return A;
    case 5:
      return B;
    case 6:
      return C;
  }

  throw "Invalid State";
}

inline int XDV(int operand) { return A / pow(2, combo(operand)); }

std::string stringify(const std::vector<int>& output) {
  std::string result;
  for (int val : output) {
    if (!result.empty()) {
      result += ",";
    }

    result += std::to_string(val);
  }

  return result;
}

std::string run(const std::vector<int>& program) {
  const int N = program.size();
  std::vector<int> output;
  for (int iptr = 0; iptr < N;) {
    switch (program[iptr]) {
      case Opcode::ADV:
        A = XDV(program[iptr + 1]);
        iptr += 2;
        break;
      case Opcode::BXL:
        B ^= program[iptr + 1];
        iptr += 2;
        break;
      case Opcode::BST:
        B = combo(program[iptr + 1]) & 7;
        iptr += 2;
        break;
      case Opcode::JNZ:
        if (A != 0) {
          iptr = program[iptr + 1];  // jump.
        } else {
          iptr += 2;
        }
        break;
      case Opcode::BXC:
        B ^= C;
        iptr += 2;
        break;
      case Opcode::OUT:
        output.emplace_back(combo(program[iptr + 1]) & 7);
        iptr += 2;
        break;
      case Opcode::BDV:
        B = XDV(program[iptr + 1]);
        iptr += 2;
        break;
      case Opcode::CDV:
        C = XDV(program[iptr + 1]);
        iptr += 2;
        break;
    }
  }

  return stringify(output);
}

int main() {
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Unable to open input.txt" << std::endl;
    return 1;
  }

  std::string line;

  // Init machine.
  std::getline(file, line);
  A = std::stoi(splitInput(line));

  std::getline(file, line);
  B = std::stoi(splitInput(line));

  std::getline(file, line);
  C = std::stoi(splitInput(line));

  std::getline(file, line);  // Empty line.
  std::getline(file, line);
  auto program = parseProgram(splitInput(line));

  std::cout << "Part 1: " << run(program) << std::endl;
}
