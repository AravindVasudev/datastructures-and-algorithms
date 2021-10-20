# https://leetcode.com/problems/prefix-and-suffix-search/
class WordFilter:
    def __init__(self, words: List[str]):
        self.mappings = {}
        for weight, word in enumerate(words):
            prefix = ""
            for pre in [""] + list(word):
                prefix += pre
                
                suffix = ""
                for suf in [""] + list(word[::-1]):
                    suffix += suf
                    self.mappings[f"{prefix}.{suffix[::-1]}"] = weight

    def f(self, prefix: str, suffix: str) -> int:
        return self.mappings.get(f"{prefix}.{suffix}", -1)
