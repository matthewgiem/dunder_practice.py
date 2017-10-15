class numString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value or isinstance(other, float):
            return float(self) + float(other)
        else:
            return int(self) + int(other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value
