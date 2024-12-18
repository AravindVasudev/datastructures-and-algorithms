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

using Register = long;
Register A, B, C;

inline std::string splitInput(const std::string& input) {
  return input.substr(input.find(": ") + 2);
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

inline long combo(int operand) {
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

inline long XDV(int operand) { return A / pow(2, combo(operand)); }

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

long part2(const std::vector<int>& program, const int idx = 0,
           const long start = 0) {
  /*
   * Input Code:
   * 2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0
   *
   * 0. BST 4: B = A & 7.
   * 1. BXL 7: B ^= 7.
   * 2. CDV 5: C = A / 2**B.
   * 3. ADV 3: A = A / 8. (or A & 7)
   * 4. BXC 4: B ^= C.
   * 5. BXL 7: B ^= 7.
   * 6. OUT 5: print(B & 7).
   * 7. JNZ 0: goto 0.
   * ====
   * B = (A & 7) ^ 7 ^ (A / 2**((A & 7) ^ 7)) ^ 7
   * print(B & 7)
   * A /= 8
   * if A: goto 0
   */
  if (idx < 0) {
    return start;  // done.
  }

  for (long i = 0; i < 8; i++) {
    const long a = start * 8 + i;
    const long b = (a & 7) ^ (a / static_cast<long>(pow(2, (a & 7) ^ 7)));
    if ((b & 7) == program[idx]) {
      if (long ret = part2(program, idx - 1, a); ret >= 0) {
        return ret;
      }
    }
  }

  return -1;
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
  A = std::stol(splitInput(line));

  std::getline(file, line);
  B = std::stol(splitInput(line));

  std::getline(file, line);
  C = std::stol(splitInput(line));

  std::getline(file, line);  // Empty line.
  std::getline(file, line);
  auto tape = splitInput(line);
  auto program = parseProgram(tape);

  std::cout << "Part 1: " << run(program) << std::endl;
  std::cout << "Part 2: " << part2(program, program.size() - 1) << std::endl;
}
