import random

from refactor.factory.bin_factory import BinFactory
from refactor.factory.trash_factory import TrashFactory
from refactor.impl.aluminium import Aluminium
from refactor.impl.glass import Glass
from refactor.impl.paper import Paper
from refactor.recycler import RecycleA

if __name__ == '__main__':
    trash_factory = TrashFactory()
    trash_factory.register_creator(0, Aluminium)
    trash_factory.register_creator(1, Paper)
    trash_factory.register_creator(2, Glass)

    bin_factory = BinFactory()

    recycler = RecycleA(trash_factory, bin_factory)

    for i in range(30):
        recycler.append_trash(
            trash_type=int(random.random() * 3),
            weight=random.random()*100
        )

    recycler.test()