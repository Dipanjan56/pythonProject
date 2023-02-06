from dateutil import parser
from datetime import datetime, timedelta


class UtilHelper:
    @staticmethod
    def increment_datetime(date_str: str, mintues: int) -> datetime:
        new_datetime = parser.parse(date_str) + timedelta(minutes=mintues)
        return new_datetime

    @staticmethod
    def convert_datetime_into_slack_reminder_dattime(date_time: datetime) -> str:
        time = datetime.strftime(date_time, "%I:%M %p")
        date = datetime.strftime(date_time, "%d-%m-%y")
        todays_date = datetime.now().strftime('%d-%m-%y')

        date_string = ''
        if todays_date == date:
            date_string = f'{time} today'

        return date_string

