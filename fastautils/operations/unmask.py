import numpy as np

from ..core import Sequence


def unmask(masked_sequence: Sequence, reference_sequence: Sequence) -> Sequence:
    unmasked_sequence = Sequence(masked_sequence.name, np.copy(masked_sequence.sequence))
    n_indexes = np.where((masked_sequence.sequence == "N") | (masked_sequence.sequence == "n"))[0]
    unmasked_sequence.sequence[n_indexes] = reference_sequence.sequence[n_indexes]
    return unmasked_sequence
