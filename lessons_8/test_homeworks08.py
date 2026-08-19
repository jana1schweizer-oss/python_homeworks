def test_main_example(self):
    total, refuels = calculate_fuel(1600, 9, 48)
    self.assertAlmostEqual(total, 144)
    self.assertAlmostEqual(refuels, 3)
def test_small_trip(self):
    total, refuels = calculate_fuel(100, 9, 48)
    self.assertAlmostEqual(total, 9)
    self.assertAlmostEqual(refuels, 0.1875)
def test_zero_distance(self):
    total, refuels = calculate_fuel(0, 9, 48)
    self.assertEqual(total, 0)
    self.assertEqual(refuels, 0)
def test_big_tank(self):
    total, refuels = calculate_fuel(500, 9, 100)
    self.assertAlmostEqual(total, 45)
    self.assertAlmostEqual(refuels, 0.45)
def test_small_tank(self):
    total, refuels = calculate_fuel(500, 9, 20)
    self.assertAlmostEqual(total, 45)
    self.assertAlmostEqual(refuels, 2.25)
def test_high_consumption(self):
    total, refuels = calculate_fuel(200, 20, 50)
    self.assertAlmostEqual(total, 40)
    self.assertAlmostEqual(refuels, 0.8)
def test_low_consumption(self):
    total, refuels = calculate_fuel(200, 5, 50)
    self.assertAlmostEqual(total, 10)
    self.assertAlmostEqual(refuels, 0.2)
def test_float_values(self):
    total, refuels = calculate_fuel(123.5, 7.2, 40.5)
    self.assertAlmostEqual(total, (123.5 / 100) * 7.2)
    self.assertAlmostEqual(refuels, total / 40.5)
def test_negative_distance(self):
    total, refuels = calculate_fuel(-100, 9, 48)
    self.assertAlmostEqual(total, -9)
    self.assertAlmostEqual(refuels, -0.1875)
