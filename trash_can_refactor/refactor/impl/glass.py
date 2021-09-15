from refactor.trash import Trash


class Glass(Trash):
    val = 0.23

    def __init__(self, wt):
        Trash.__init__(self, wt)

    def get_value(self):
        return self.val

    def setValue(self, newval):
        val = newval