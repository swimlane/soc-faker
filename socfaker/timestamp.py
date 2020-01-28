import pendulum
import random

class Timestamp(object):


    def in_the_past(self,
        years=0, 
        months=1, 
        days=random.randint(1,15), 
        hours=random.randint(1,24),
        minutes=random.randint(1,60),
        seconds=random.randint(1,60)):
        return pendulum.now().subtract(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds).to_iso8601_string()

    def in_the_future(self,
        years=0, 
        months=1, 
        days=random.randint(1,15), 
        hours=random.randint(1,24),
        minutes=random.randint(1,60),
        seconds=random.randint(1,60)):
        return pendulum.now().add(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds).to_iso8601_string()
    @property
    def current(self):
        return pendulum.now().to_iso8601_string()
