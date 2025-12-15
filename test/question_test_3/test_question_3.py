
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.question_3.question_3 import (
    get_most_likely_ancestor_consensus,
    get_most_likely_ancestor_consenus,
)

def test_sample_dataset_main_function():
    dna1 = "GATATATGCATATACTT"
    dna2 = "ATAT"
    result = get_most_likely_ancestor_consensus(dna1, dna2)
    assert result == (2, 4, 10)

def test_sample_dataset_misspelled_function_name():
    dna1 = "GATATATGCATATACTT"
    dna2 = "ATAT"
    result = get_most_likely_ancestor_consenus(dna1, dna2)
    assert result == (2, 4, 10)

def test_no_occurrences():
    result = get_most_likely_ancestor_consensus("AAAAAAAAAAAAA", "TTTT")
    assert result == ()
