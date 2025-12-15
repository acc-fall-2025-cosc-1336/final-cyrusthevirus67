
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.question_1.question_1 import create_mulitiplication_table

def test_create_multiplication_table_shape():
    table = create_mulitiplication_table()
    assert len(table) == 5
    for row in table:
        assert len(row) == 10

def test_create_multiplication_table_values():
    table = create_mulitiplication_table()
    assert table[0] == [1,2,3,4,5,6,7,8,9,10]
    assert table[1] == [2,4,6,8,10,12,14,16,18,20]
    assert table[4] == [5,10,15,20,25,30,35,40,45,50]
