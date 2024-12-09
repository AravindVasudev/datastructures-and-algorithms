/*
$ hyperfine --runs 10 ./day_9
Benchmark 1: ./day_9
  Time (mean ± σ):     127.6 ms ±   0.3 ms    [User: 125.7 ms, System: 1.3 ms]
  Range (min … max):   127.1 ms … 128.0 ms    10 runs
*/

#include <fstream>
#include <iostream>
#include <tuple>
#include <unordered_map>

const int FREE = -1;

std::tuple<std::vector<int>, std::vector<int>, std::unordered_map<int, int>>
decompress(const std::string& dskmap) {
  std::vector<int> dsk, freeSize;  // freeSize suffixSum of free space.
  std::unordered_map<int, int> blockSize;
  int id = 0;
  bool used = true;

  for (char c : dskmap) {
    const int numBlocks = (c - '0');  // To int.
    for (int i = 0; i < numBlocks; i++) {
      dsk.push_back(used ? id : FREE);
      freeSize.push_back(used ? 0 : numBlocks - i);
    }

    if (used) {
      blockSize[id] = numBlocks;
      id++;
    }

    used = !used;
  }

  return {dsk, freeSize, blockSize};
}

void compact1(std::vector<int>& dsk) {
  const int N = dsk.size();
  int free = 0, end = N - 1;

  while (free < end) {
    // find free.
    while (free < N && dsk[free] != FREE) {
      free++;
    }

    // find end.
    while (end >= 0 && dsk[end] == FREE) {
      end--;
    }

    if (free >= end) {
      break;
    }

    dsk[free] = dsk[end];
    dsk[end] = FREE;
  }
}

long checksum(const std::vector<int>& dsk) {
  const int N = dsk.size();
  long checksum = 0;
  for (int i = 0; i < N; i++) {
    if (dsk[i] == FREE) {
      continue;
    }

    checksum += dsk[i] * i;
  }

  return checksum;
}

long part1(const std::string& dskmap) {
  std::vector<int> dsk;
  std::tie(dsk, std::ignore, std::ignore) = decompress(dskmap);
  compact1(dsk);
  return checksum(dsk);
}

int findNextBlock(const std::vector<int>& dsk, int segment) {
  while (segment > 0 && dsk[segment] == FREE) {
    segment--;
  }

  return segment;
}

void compact2(std::vector<int>& dsk, const std::vector<int>& freeSizes,
              const std::unordered_map<int, int>& blockSizes) {
  const int N = dsk.size();
  int block = N - 1;

  while (block > 0) {
    block = findNextBlock(dsk, block);
    int id = dsk[block], usedSize = blockSizes.at(id);
    bool moved = false;

    // Find free spot.
    for (int free = 0; free < block;) {
      while (free < block && dsk[free] != FREE) {
        free++;  // find free.
      }

      if (free >= block) {
        break;
      }

      int freeSize = freeSizes[free];
      if (freeSize >= usedSize) {
        // Move
        while (free < block && dsk[block] == id) {
          dsk[free++] = id;
          dsk[block--] = FREE;
        }

        moved = true;
        break;
      }

      free += freeSize;  // skip this and search for the next free block.
    }

    // Skip this used block if it cannot be moved.
    if (!moved) {
      int start = block - usedSize;
      while (start >= 0 && dsk[start] == FREE) {
        start--;
      }

      block = start;
    }
  }
}

long part2(const std::string& dskmap) {
  auto [dsk, freeSize, blockSize] = decompress(dskmap);
  compact2(dsk, freeSize, blockSize);
  return checksum(dsk);
}

int main() {
  std::ifstream input("input.txt");
  if (!input.is_open()) {
    std::cerr << "Error: Unable to open input.txt" << std::endl;
    return 1;
  }

  std::string dskmap;
  getline(input, dskmap);
  input.close();

  std::cout << "Part 1: " << part1(dskmap) << std::endl;
  std::cout << "Part 2: " << part2(dskmap) << std::endl;
}
