def print_owing(self):
    self.print_banner()
    self.print_details()

def print_details(self):
    print("name:", self.name)
    print("amount:", self.get_outstanding())