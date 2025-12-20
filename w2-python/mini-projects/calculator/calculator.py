class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b