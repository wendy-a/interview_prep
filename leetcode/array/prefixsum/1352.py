class ProductOfNumbers:

    def __init__(self):
        self.preproduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.preproduct = [1]
        else:
            self.preproduct.append(self.preproduct[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.preproduct)
        if k > n - 1:
            return 0
        else:
            return self.preproduct[-1] // self.preproduct[n - k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)