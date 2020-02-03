from typing import List

import numpy as np

from ..core import Sequence

# TODO: Add support fot other fasta file type
VALID_FILE_EXTENSIONS = (".fasta", ".fna")


def is_valid_file_extension(filename: str) -> bool:
    for extension in VALID_FILE_EXTENSIONS:
        if not filename.endswith(extension):
            return True
    return False


def is_valid_number_of_lines_in_file(sequences_in_file_count: int):
    if sequences_in_file_count % 2 == 0:
        return True
    return False


def read_fasta_file(filename: str) -> List[Sequence]:
    if not is_valid_file_extension(filename):
        raise IOError("Not valid file extension")
    with open(filename) as sequence_file:
        lines = sequence_file.readlines()
    if not is_valid_number_of_lines_in_file(len(lines)):
        raise IOError("File doesn't have correct format")
    sequences_in_file_count = int(len(lines)/2)
    sequences = []
    for i_experiment in range(sequences_in_file_count):
        name = lines[i_experiment*2].strip()
        sequence = lines[i_experiment*2+1].strip()
        sequence = np.array(list(sequence))
        sequences.append(Sequence(name, sequence))
    return sequences
