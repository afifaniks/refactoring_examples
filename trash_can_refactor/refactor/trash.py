from abc import ABC
from abc import abstractmethod


class Trash(ABC):
    def __init__(self, weight):
        self.weight = weight

    @abstractmethod
    def get_value(self):
        pass

    def get_weight(self):
        return self.weight