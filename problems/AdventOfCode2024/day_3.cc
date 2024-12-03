#include <iostream>
#include <fstream>
#include <regex>

int parseCorruptedSubString(std::string::const_iterator begin, std::string::const_iterator end) {
    std::regex mulPattern("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)");
    std::smatch match;
    int result = 0;

    auto it = begin;
    while (std::regex_search(it, end, match, mulPattern)) {
        result += std::stoi(match[1].str()) * std::stoi(match[2].str());
        it = match.suffix().first;
    }


    return result;
}

int parseCorruptedInstructionI(const std::string& instruction) {
    return parseCorruptedSubString(instruction.cbegin(), instruction.cend());
}

int parseCorruptedInstructionII(const std::string& instruction) {
    std::regex dontPattern("don't\\(\\)");
    std::regex doPattern("do\\(\\)");
    std::smatch match;
    int result = 0;

    bool enabled{true};
    auto it = instruction.cbegin();

    while (it != instruction.cend()) {
        if (enabled) {
            std::regex_search(it, instruction.cend(), match, dontPattern);
            result += parseCorruptedSubString(it, match.suffix().first);
            enabled = false;
            it = match.suffix().first;
        } else {
            std::regex_search(it, instruction.cend(), match, doPattern);
            enabled = true;
            it = match.suffix().first;
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

    std::string completeInstruction;
    std::string instruction;
    while (std::getline(input, instruction)) {
        completeInstruction += instruction;
    }

    std::cout << "Parsed Multiplication Result: " << parseCorruptedInstructionI(completeInstruction) << std::endl;
    std::cout << "Parsed Multiplication Result II: " << parseCorruptedInstructionII(completeInstruction) << std::endl;
}
