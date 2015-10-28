#https://www.hackerrank.com/challenges/calendar-module

import calendar

the_date = list(raw_input().split(" "))


# calendar.weekday(year, month, day), 0 is Monday...
our_weekday = calendar.weekday(int(the_date[2]), int(the_date[0]), int(the_date[1]))


day_of_week_dict = {
	"0":"MONDAY",
	"1":"TUESDAY",
	"2":"WEDNESDAY",
	"3":"THURSDAY",
	"4":"FRIDAY",
	"5":"SATURDAY",
	"6":"SUNDAY",


}

print day_of_week_dict[str(our_weekday)]
