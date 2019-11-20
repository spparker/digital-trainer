from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

class Programmer:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.days = {}

    def create_program(self):
        for day in daterange(self.start_date, self.end_date):
            #print(day.strftime("%Y-%m-%d"))
            self.days[day] = 'rest'

        for d in self.days:
            print(d)
            print(self.days[d])

p = Programmer(date(2019,11,14), date(2019,12,14))
p.create_program()

