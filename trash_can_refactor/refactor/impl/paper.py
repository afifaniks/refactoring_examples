from refactor.trash import Trash


class Paper(Trash):
    val = 0.10

    def __init__(self, wt):
        Trash.__init__(self, wt)

    def get_value(self):
        return self.val

    def setValue(self, newval):
        val = newval