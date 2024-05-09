#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from simple_calculator.main import SimpleCalculator

def test_add_two_numbers():
    calculator = SimpleCalculator()

    result=calculator.add(4,5)

    assert result==9

def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 6)

    assert result == 15

def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.sub(10, 3)

    assert result == 7

def test_mul_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.mul(6, 4)

    assert result == 24

def test_mul_many_numbers():
    numbers = range(1, 10)

    calculator = SimpleCalculator()

    result = calculator.mul(*numbers)

    assert result == 362880

def test_div_two_numbers_float():
    calculator= SimpleCalculator()

    result = calculator.div(1,2)

    assert result==0.5

def test_div_by_zero_returns_inf():
    calculator = SimpleCalculator()

    result = calculator.div(5, 0)

    assert result == float('inf')

def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.mul(3, 0)

#my test for part II
def test_compute_avg_iterable():
    calculator= SimpleCalculator()

    result=calculator.avg([2,5,12,98])

    assert result == 29.25

def test_compute_avg_iterable_optional_ut():
    calculator= SimpleCalculator()

    result = calculator.avg([2,5,12,98],90)

    assert result == 6.33

def test_compute_avg_iterable_optional_lt():
    calculator= SimpleCalculator()

    result = calculator.avg([2,5,12,15,98],90,11)

    assert result==13.5

def test_compute_avg_iterable_optional_ut_not_included():
    calculator= SimpleCalculator()

    result = calculator.avg([2,5,12,15,98],12)

    assert result == 6.33

def test_compute_avg_iterable_optional_lt_not_included():
    calculator= SimpleCalculator()

    result = calculator.avg([2,5,12,15,98],lt=15)

    assert result == 56.5

def test_compute_avg_iterable_empty():
    calculator= SimpleCalculator()

    result = calculator.avg([])

    assert result == 0

def test_compute_avg_iterable_after_oulier_removal():
    calculator= SimpleCalculator()

    result = calculator.avg([12,98],ut=90,lt=15)

    assert result == 0

def test_compute_avg_iterable_empty_oulier_removal():
    #probablemente esta prueba esta de mas
    calculator= SimpleCalculator()

    result = calculator.avg([],ut=90,lt=15)

    assert result == 0