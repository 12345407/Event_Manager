from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        title = ''
        delete = ''
        for event in events_per_day:

            title += f'<li class="date"> {event.get_html_url} </li>'
            delete += f'<li class="date"> {event.get_url} </li>'

        if day != 0:
            return f"<td><span class='date '>{day}</span><ul> {title} {delete} </ul></td>\n"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(
            start_time__year=self.year, start_time__month=self.month)

        dashboard = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        dashboard += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        dashboard += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            dashboard += f'{self.formatweek(week, events)}\n'
        return dashboard
