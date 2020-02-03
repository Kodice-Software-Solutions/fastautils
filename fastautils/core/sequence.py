import numpy as np


class Sequence:
    def __init__(self, name: str, sequence: np.array):
        self._name = name
        self._sequence = sequence

    @property
    def name(self):
        return self._name

    @property
    def sequence(self):
        return self._sequence
