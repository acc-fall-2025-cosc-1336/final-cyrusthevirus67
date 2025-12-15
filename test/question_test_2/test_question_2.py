
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.question_2.question_2 import Stock, get_stock_list

def test_stock_class_getters():
    s = Stock("AAPL", "Apple Inc")
    assert s.get_symbol() == "AAPL"
    assert s.get_company_name() == "Apple Inc"

def test_get_stock_list_contents():
    stocks = get_stock_list()
    assert len(stocks) == 5
    data = {s.get_symbol(): s.get_company_name() for s in stocks}
    assert data["AAPL"] == "Apple Inc"
    assert data["CAT"] == "Caterpillar"
    assert data["EK"] == "Eastman Kodak"
    assert data["GOOG"] == "Google"
    assert data["MSFT"] == "Microsoft"
