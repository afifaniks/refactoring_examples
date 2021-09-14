from refactor.trash import Trash


class Aluminium(Trash):
    val = 1.67

    def __init__(self, wt):
        Trash.__init__(self, wt)

    def get_value(self):
        return self.val

    def setValue(newval):
        val = newval