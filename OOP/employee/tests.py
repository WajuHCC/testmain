from employee import Employee

class TestEmployee:

    def test_init(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.first_name == "Jan"
        assert e.last_name == "Kowalski"
        assert e.rate_per_hour == 100

    def test_register_time(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e._registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

from employee import PremiumEmployee

class TestPremiumEmployee:

    def test_init(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        assert e.first_name == "Jan"
        assert e.last_name == "Kowalski"
        assert e.rate_per_hour == 100

    def test_register_time(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e._registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

    def test_give_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.give_bonus(1000)
        assert e.bonuses ==[1000]

    # def test_pay_salary_with_bonus(self):
    #     e = PremiumEmployee("Jan", "Kowalski", 100)
    #     e.register_time(6)
    #     e.give_bonus(1000)
    #     assert e.pay_salary() == 1600

    def test_pay_salary_with_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(6)
        e.give_bonus(1000)
        e.give_bonus(0.1)
        assert e.pay_salary() == 1660