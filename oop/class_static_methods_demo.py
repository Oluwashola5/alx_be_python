class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method - does not access or modify class or instance data
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method - has access to class data and can modify class state
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
