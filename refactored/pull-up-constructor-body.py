class Manager(Employee):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade