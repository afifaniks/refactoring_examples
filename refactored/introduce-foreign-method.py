class Report:
    def send_report(self):
        nextDay = self.get_next_day()
    
    def get_next_day(self):
        return Date(self.previousEnd.getYear(),
            self.previousEnd.getMonth(), self.previousEnd.getDate() + 1)