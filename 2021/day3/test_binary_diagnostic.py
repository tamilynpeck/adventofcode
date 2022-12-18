from binary_diagnostic import BinaryDiagnostic


test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

diagnostic = BinaryDiagnostic(test_input)

def test_gamma_rate():
    
    assert diagnostic.gamma == '10110'
    assert int(diagnostic.gamma, 2) == 22
    assert diagnostic.epsilon == '01001'
    assert int(diagnostic.epsilon, 2) == 9
    assert diagnostic.power_consumption == 198

    assert diagnostic.oxygen_generator_rating == "10111"
    assert int(diagnostic.oxygen_generator_rating, 2) == 23
    assert diagnostic.c02_scrubber == "01010"
    assert int(diagnostic.c02_scrubber, 2) == 10
    assert diagnostic.life_support_rating == 230