class frange:
    def __init__(self, left, right=None, step=None):
        self._left = left
        self._right = right
        self._step = step
        if self._right is None:
            self._left, self._right = 0, self._left
        self.cnt = 1 if self._left > self._right else 0
        if not step:
            if self._left <= self._right:
                self._step = 1
            else:
                self._step = None

    def __next__(self):
        if self.cnt == 0:
            if self._left < self._right:
                res = self._left
                self._left += self._step
                return res
            else:
                raise StopIteration
        elif self.cnt == 1:
            if self._step is not None:
                if self._right < self._left:
                    res = self._left
                    self._left += self._step
                    return res
                else:
                    raise StopIteration
            else:
                raise StopIteration

    def __iter__(self):
        return self


assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []

print("SUCCESS!")
