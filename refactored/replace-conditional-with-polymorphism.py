from abc import ABCMeta

class Bird(metaclass=ABCMeta):
    def get_speed(self):
        return self.get_base_speed()

    def get_base_speed(self):
        return 1


class EuropeanBird(Bird):
    pass


class AfricanBird(Bird):
    def get_speed(self):
        return self.get_base_speed() - self.get_load_factor() * self.num_of_cocunuts


class NorwegianBlue(Bird):
    self.is_nailed = True
    
    def get_base_speed(self, voltage):
        return 1

    def get_speed(self):
        return 0 if self.is_nailed else self.get_base_speed(1)