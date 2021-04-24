class CellGroup:
    def __init__(self):
        self._cells = set()

    def __str__(self) -> str:
        return str(self._cells)

    def __repr__(self) -> str:
        return self.__str__()

    def __contains__(self, item) -> bool:
        return self._cells.__contains__(item)

    def insert(self, candidate: int) -> bool:
        if (not isinstance(candidate, int)) or (not 1 <= candidate <= 9):
            raise ValueError('Expected integer between 1 & 9 inclusive')

        if candidate in self._cells:
            return False

        self._cells.add(candidate)
        return True

