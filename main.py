# Your task is to extend its functionality with a new method called count_weekday_in_year, which takes a
# year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.
from calendar import Calendar
class MyCalendar(Calendar):
    def __init__(self):
        super().__init__()
    
    def countWeekdatInYear(self,y,wd):
        count = 0 
        for x in range(1,13):
            for i in self.monthdays2calendar(y,x):
                for z in i:
                    if z[0]!=0 and z[1]==wd:
                        count+=1
        print(count)

c = MyCalendar()

c.countWeekdatInYear(2019,0)