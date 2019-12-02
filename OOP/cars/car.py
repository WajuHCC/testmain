class ElectricCar:
    def __init__(self, range):
        self.max_range = range
        self.counter = 0

    def drive(self, distance):
        if self.counter + distance < self.max_range:
            self.counter += distance
            to_travel = distance
        else:
            to_travel = self.max_range - self.counter
            self.counter = self.max_range
        return to_travel

    def charge(self):
        self.counter = 0

