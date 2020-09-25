class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def validate(date_in_parts):
        print(f'Day value {date_in_parts[0]} is correct (from 1 to 31)' if 0 < date_in_parts[
            0] <= 31 else f'Day value {date_in_parts[0]} is out of range!')
        print(f'Month value {date_in_parts[1]} is correct (from 1 to 12)' if 0 < date_in_parts[
            1] <= 12 else f'Month value {date_in_parts[1]} is out of range!')
        print(f'Year value {date_in_parts[2]} is correct (from 1 to 9999)' if 0 < date_in_parts[
            2] <= 9999 else f'Year value {date_in_parts[2]} is out of range!')


print(Date.to_int('11-03-1994'))
Date.validate(Date.to_int('11-03-1994'))
