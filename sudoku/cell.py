class Cell:
    def __init__(self, value: int = 0):
        self.value = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        if (not isinstance(value, int)) or (not 0 <= value <= 9):
            raise ValueError('Expected integer between 0 & 9 inclusive')

        self._value = value
