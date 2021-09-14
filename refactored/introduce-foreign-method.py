class Report:
    def send_report(self):
        nextDay = self.get_next_day()
    
    def get_next_day(self): # Comment: I think it would be better to extend the Date class
        return Date(self.previousEnd.getYear(),
            self.previousEnd.getMonth(), self.previousEnd.getDate() + 1)