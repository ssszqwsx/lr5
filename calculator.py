class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    def power(self, base: int, exp: int) -> int:
        if base == 0 and exp == 0:
            raise ValueError("0 to the power of 0 is undefined")
        return base ** exp

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def lcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.gcd(a, b)