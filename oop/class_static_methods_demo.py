class Calculator:
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        if not isinstance(a, (int,float)):
            raise TypeError('a should be an integer or float')
        if not isinstance(b, (int, float)):
            raise TypeError('b shoudl be an integer of float value')
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    
