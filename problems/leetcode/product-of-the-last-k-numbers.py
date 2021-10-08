# https://leetcode.com/problems/product-of-the-last-k-numbers/
class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]
        else:
            self.prefixProduct.append(num * self.prefixProduct[-1])

    def getProduct(self, k: int) -> int:
        return self.prefixProduct[-1] // self.prefixProduct[-k-1] if k < len(self.prefixProduct) else 0
