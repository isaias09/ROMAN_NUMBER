from roman_funcs import num_to_roman
def test_romanos_sipmles():
    assert num_to_roman(1) == 'I'
    assert num_to_roman(5) == 'V'
    assert num_to_roman(10) == 'X'
    assert num_to_roman(50) == 'L'
    assert num_to_roman(100) == 'C'
    assert num_to_roman(500) == 'D'
    assert num_to_roman(1000) == 'M'

