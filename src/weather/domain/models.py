from datetime import datetime


class Temp:
    '''
    Represents the temperature data at specific time 
    and at a specific location(city).
    '''
    def __init__(
            self,
            datetime: datetime,
            value: float,
            location: str,
    ) -> None:
        self.datetime: datetime = datetime
        self.value: float = value
        self.location: str = location


    def __repr__(self) -> str:
        f_str = 'Temp(datetime="{}", value={}, location="{}")'
        return f_str.format(self.datetime, self.value, self.location)
