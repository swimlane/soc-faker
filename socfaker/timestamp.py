import pendulum
from .baseclass import BaseClass

class Timestamp(BaseClass):

    """The Timestamp Class provides methods to generate timestamps
    """

    def in_the_past(self,
        years=0, 
        months=BaseClass().random.randint(0,3),
        days=BaseClass().random.randint(1,15), 
        hours=BaseClass().random.randint(1,24),
        minutes=BaseClass().random.randint(1,60),
        seconds=BaseClass().random.randint(1,60)):
        """Generates a timestamp in the past

        Args:
            years (int, optional): The number of years to subtract from the current time. Defaults to 0.
            months ([type], optional): The number of months to subtract from the current time. Defaults to random.randint(0,3).
            days ([type], optional): The number of days to subtract from the current time. Defaults to random.randint(1,15).
            hours ([type], optional): The number of hours to subtract from the current time. Defaults to random.randint(1,24).
            minutes ([type], optional): The number of minutes to subtract from the current time. Defaults to random.randint(1,60).
            seconds ([type], optional): The number of seconds to subtract from the current time. Defaults to random.randint(1,60).

        Returns:
            str: Returns an ISO 8601 timestamp string
        """
        return pendulum.now().subtract(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds).to_iso8601_string()

    def in_the_future(self,
        years=0,
        months=BaseClass().random.randint(0,3),
        days=BaseClass().random.randint(1,15), 
        hours=BaseClass().random.randint(1,24),
        minutes=BaseClass().random.randint(1,60),
        seconds=BaseClass().random.randint(1,60)):
        """Generates a timestamp in the future

        Args:
            years (int, optional): The number of years to add from the current time. Defaults to 0.
            months ([type], optional): The number of months to add from the current time. Defaults to random.randint(0,3).
            days ([type], optional): The number of days to add from the current time. Defaults to random.randint(1,15).
            hours ([type], optional): The number of hours to add from the current time. Defaults to random.randint(1,24).
            minutes ([type], optional): The number of minutes to add from the current time. Defaults to random.randint(1,60).
            seconds ([type], optional): The number of seconds to add from the current time. Defaults to random.randint(1,60).

        Returns:
            str: Returns an ISO 8601 timestamp string
        """
        return pendulum.now().add(
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds).to_iso8601_string()

    @property
    def current(self):
        """The current timestamp

        Returns:
            str: Returns the current timestamp in ISO 8601 format
        """
        return pendulum.now().to_iso8601_string()

    def date_string(self,
        years=BaseClass().random.randint(18,85), 
        months=BaseClass().random.randint(1,12),
        days=BaseClass().random.randint(1,365)):
        """Returns a date string

        Args:
            years ([type], optional): The number of years subtracted from the current time. Defaults to random.randint(18,85).
            months ([type], optional): The number of months subtracted from the current time. Defaults to random.randint(1,12).
            days ([type], optional): The number of days subtracted from the current time. Defaults to random.randint(1,365).

        Returns:
            str: An date string for the generated timestamp
        """
        return pendulum.now().subtract(years=years, months=months, days=days).to_date_string()
