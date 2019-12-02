from car import ElectricCar

class TestElectricCar:

    def test_init(self):
        c = ElectricCar(100)
        assert c.max_range == 100

    def test_drive_below_max_range(self):
        c = ElectricCar(100)
        assert c.drive(70) == 70

    def test_drive_over_max_range(self):
        c = ElectricCar(100)
        assert c.drive(70) == 70
        assert c.drive(50) == 30
        assert c.drive(50) == 0

    def test_charge(self):
        c = ElectricCar(100)
        assert c.drive(70) == 70
        assert c.drive(50) == 30
        assert c.drive(50) == 0
        c.charge()
        assert c.drive(50) == 50