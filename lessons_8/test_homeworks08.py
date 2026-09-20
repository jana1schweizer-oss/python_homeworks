from lessons_8.homeworks import calculate_fuel


def test_main_example():
    total, refuels = calculate_fuel(1600, 9, 48)
    assert total == 144
    assert refuels == 3

def test_small_trip():
    total, refuels = calculate_fuel(100, 9, 48)
    assert total == 9
    assert refuels == 0.1875

def test_zero_distance():
    total, refuels = calculate_fuel(0, 9, 48)
    assert total == 0
    assert refuels == 0

def test_big_tank():
    total, refuels = calculate_fuel(500, 9, 100)
    assert total == 45
    assert refuels == 0.45

def test_small_tank():
    total, refuels = calculate_fuel(500, 9, 20)
    assert total == 45
    assert refuels == 2.25

def test_high_consumption():
    total, refuels = calculate_fuel(200, 20, 50)
    assert total == 40
    assert refuels == 0.8

def test_low_consumption():
    total, refuels = calculate_fuel(200, 5, 50)
    assert total == 10
    assert refuels == 0.2

def test_float_values():
    total, refuels = calculate_fuel(123.5, 7.2, 40.5)
    assert total == (123.5 / 100) * 7.2
    assert refuels == total / 40.5

def test_negative_distance():
    total, refuels = calculate_fuel(-100, 9, 48)
    assert total == -9
    assert refuels == -0.1875

def test_negative_tank():
    total, refuels = calculate_fuel(500, 9, -48)
    assert total == 45
    assert refuels == -0.9375

