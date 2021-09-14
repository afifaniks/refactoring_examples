from refactor.factory.bin_factory import BinFactory
from refactor.factory.trash_factory import TrashFactory
from refactor.impl.aluminium import Aluminium
from refactor.impl.glass import Glass
from refactor.impl.paper import Paper
from refactor.services.weight_sum_service import WeightSumService


class RecycleA:
    def __init__(self,
                 trash_factory: TrashFactory,
                 bin_factory: BinFactory):
        # Fill up the Trash bin:
        self.bins = []
        self.glass_bin = []
        self.paper_bin = []
        self.alu_bin = []

        self.trash_factory = trash_factory
        self.bin_factory = bin_factory

    def append_trash(self, trash_type: int, weight: float) -> None:
        self.bins.append(self.trash_factory.create(trash_type, wt=weight))

    def test(self):
        for bin in self.bins:
            if isinstance(bin, Aluminium):
                self.alu_bin.append(bin)
            elif isinstance(bin, Paper):
                self.paper_bin.append(bin)
            elif isinstance(bin, Glass):
                self.glass_bin.append(bin)

        print(f"Total Value: {WeightSumService.calculate_weight(self.alu_bin)}")
        print(f"Total Value: {WeightSumService.calculate_weight(self.paper_bin)}")
        print(f"Total Value: {WeightSumService.calculate_weight(self.glass_bin)}")
        print("\n")
        print(f"Total Value: {WeightSumService.calculate_weight(self.bins)}")
