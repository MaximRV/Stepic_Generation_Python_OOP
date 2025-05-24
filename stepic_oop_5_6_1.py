class Calculator:
    def __call__(self, a, b, operation):
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b:a / b
        }
        try:
            result = operations[operation](a, b)
            return result
        except ZeroDivisionError as e:
            raise ValueError("Деление на ноль невозможно")
