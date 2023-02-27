
class Date:
    def __init__(self, year, month, day, week):
        self.year = year
        self.month = month
        self.day = day
        self.week = week
        self.days_list = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 100 == 0 and self.year % 400 == 0):
            self.days_list[2] = 29
        else:
            self.days_list[2] = 28

    def one_step_date(self):
        self.day += 1
        self.week += 1
        self.week %= 7

        if self.month == 12 and self.day > self.days_list[12]:
            self.year += 1
            self.month = 1
            self.day = 1
            if self.year % 4 == 0 and self.year % 400 != 0:
                self.days_list[2] = 29
            else:
                self.days_list[2] = 28
        elif self.day > self.days_list[self.month]:
            self.month += 1
            self.day = 1
        else:
            pass
    def compareTo(self, date):
        if self.year == date.year \
            and self.month == date.month \
            and self.day == date.day:
            return True
        else:
            return False


if __name__ == '__main__':
    date = Date(1900, 1, 1, 0)
    enddate = Date(1901, 1, 1, None)
    count = 0

    while True:
        print(date.year, date.month, date.day, date.week)
        date.one_step_date()
        if date.compareTo(enddate):
            break
    enddate = Date(2001, 1, 1, None)
    while True:
        print(date.year, date.month, date.day, date.week)
        if date.day == 1 and date.week == 6:
            count += 1
        date.one_step_date()
        if date.compareTo(enddate):
            break

    print(count)

