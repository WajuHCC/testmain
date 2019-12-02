class Employee:

    def __init__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self._registered_hours = 0  #Shift+f6 robi refactor i zmienia wszystkie nazwy zmiennej w powiaanych plikach

    def register_time(self, time):
        self._registered_hours = time

    def pay_salary(self):
        if self._registered_hours <= 8:
            to_pay = self._registered_hours * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self._registered_hours - 8) * 2 * self.rate_per_hour
        self._registered_hours = 0
        return to_pay

emp = Employee("Jan", "Kowalski", 200)
print(emp._registered_hours)
emp._registered_hours = 10
print(emp.pay_salary())

