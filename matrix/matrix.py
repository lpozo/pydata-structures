"""Matrix abstract data type."""

from typing import Any, Tuple


class Matrix:
    """Build a matrix as an m × n rectangular grid."""

    def __init__(self, rows: int, cols: int, default: int = 0) -> None:
        self._rows = rows
        self._cols = cols
        self._data = [[default] * cols for _ in range(rows)]

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def scale_by(self, scalar: int) -> None:
        for row in range(self._rows):
            for col in range(self._cols):
                self[row, col] *= scalar

    @property
    def size(self) -> Tuple[int, int]:
        return self._rows, self._cols

    def transpose(self) -> "Matrix":
        transposed = self.__class__(self._cols, self._rows)
        transposed._data = [list(row) for row in zip(*self._data)]
        return transposed

    def add(self, other) -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("can only add matrix to matrix")
        if other.size == self.size:
            matrix = self.__class__(self._rows, self._cols)
            for row in range(self._rows):
                for col in range(self._cols):
                    matrix[row, col] = self[row, col] + other[row, col]
            return matrix
        raise ValueError("invalid matrix size")

    def subtract(self, other) -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("can only subtract matrix from matrix")
        if other.size == self.size:
            matrix = self.__class__(self._rows, self._cols)
            for row in range(self._rows):
                for col in range(self._cols):
                    matrix[row, col] = self[row, col] - other[row, col]
            return matrix
        raise ValueError("invalid matrix size")

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(\n\t"
            + "\n\t".join(str(row) for row in self._data)
            + "\n)"
        )

    def mutiply(self, other) -> "Matrix":
        if not (other.__class__ is self.__class__):
            raise TypeError("can only multiply matrix by matrix")
        if self._cols == other._rows:
            matrix = self.__class__(self._rows, other._cols)
            for row in range(1):
                pass
        raise ValueError("invalid matrix size")

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(rows={self._rows}, cols={self._cols})"
        )

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = self._validate_indices(index)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = self._validate_indices(index)
        self._data[row][col] = value

    def _validate_indices(self, index: Tuple[int, int]) -> Tuple[int, int]:
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError("Invalid number of indices")
        row, col = index
        if not 0 <= row < self._rows:
            raise IndexError("Row index out of range")
        if not 0 <= col < self._cols:
            raise IndexError("Column index out of range")
        return index


m = Matrix(6, 3, 3)
print(m)
n = Matrix(3, 6, 5)
print(n)
print(n.mutiply(m))
