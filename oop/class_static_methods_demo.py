# class_static_methods_demo.py

class Calculator:
    # This is like a sign on EVERY calculator that says what kind it is
    calculation_type = "Arithmetic Operations"

    # STATIC METHOD → works without even holding a calculator!
    @staticmethod
    def add(a, b):
        return a + b
        # No "self", no "cls" → it’s just a normal function chilling inside the class

    # CLASS METHOD → needs to know what KIND of calculator we’re talking about
    @classmethod
    def multiply(cls, a, b):
        # cls means "the class itself" — in this case Calculator"
        print(f"Calculation type: {cls.calculation_type}")
        return a * b