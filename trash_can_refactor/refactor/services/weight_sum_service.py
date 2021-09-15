from typing import List

from refactor.trash import Trash


class WeightSumService:
    @staticmethod
    def log_values(trash: Trash) -> None:
        print(f"weight of {type(trash).__name__} = {trash.get_weight()}")

    @staticmethod
    def calculate_weight(trash_list: List[Trash]) -> float:
        value = 0.0

        for trash in trash_list:
            WeightSumService.log_values(trash)
            value += trash.get_weight() * trash.get_value()

        return value

