class Calculator:
    @staticmethod
    def add(*args):
        num = args[0]
        for nums in range(1, len(args)):
            num += args[nums]
        return num

    @staticmethod
    def multiply(*args):
        num = args[0]
        for nums in range(1, len(args)):
            num *= args[nums]
        return num

    @staticmethod
    def divide(*args):
        num = args[0]
        for nums in range(1, len(args)):
            num /= args[nums]
        return num

    @staticmethod
    def subtract(*args):
        num = args[0]
        for nums in range(1, len(args)):
            num -= args[nums]
        return num

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

