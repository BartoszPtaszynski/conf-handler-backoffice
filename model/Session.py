import uuid

from pyarrow import UuidType


class Session:
    def __init__(self, id: uuid.UUID, name: str, session_date, time_start, time_end, city: str, street: str, building: str, room_number: str, chairman: str):
        self.id = id
        self.name = name
        self.session_date = session_date
        self.time_start = time_start
        self.time_end = time_end
        self.city = city
        self.street = street
        self.building = building
        self.room_number = room_number
        self.chairman = chairman

    def to_dict(self):
        return {
            "id": str(self.id),  # Zamiana UUID na string
            "name": self.name,
            "session_date": (self.session_date),
            "time_start": (self.time_start),
            "time_end": (self.time_end),
            "city": self.city,
            "street": self.street,
            "building": self.building,
            "room_number": self.room_number,
            "chairman": self.chairman
        }