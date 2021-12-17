from datetime import datetime

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = ""
        self.end_time = ""
        self.is_occupied = False
        self.time_duration = 0
        self.total_cost_per_hour = 30.0
        self.total_cost = 0.0

    def check_in(self):
        print("checking in...")
        self.is_occupied = False
        self.end_time = datetime.now()
        self.time_duration = self.end_time - self.start_time
        self.total_time_minutes = self.time_duration.total_seconds()/60
        self.total_cost = round((self.total_cost_per_hour / 60) * self.total_time_minutes, 2)
        

    def check_out(self):
        print("checking out...")
        self.is_occupied = True
        self.start_time = datetime.now()