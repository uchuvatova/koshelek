from faker import Faker


class RandomData:
    def __init__(self):
        self.fake = Faker()

    @property
    def generate_random_name(self):
        return self.fake.name()

    @property
    def generate_seven_symbol_pass(self):
        return self.fake.password(7)
