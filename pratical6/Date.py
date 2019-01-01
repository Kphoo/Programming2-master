class Date:
    def _init_(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    def _str_(self):
        return "{}-{}-{}".format(self.day, self.month, self.year )


    def add_days(self, n):
        self.day += n

        if self.day <= 31:
            self.day = self.day
        elif self.day <=58:
            self.month += self.day // 31
            self.day = self.day % 30 -1
        # elif self.day <= 90:
        #     self.month += self.day // 31
        #     self.day = (self.day % 90)