import uuid
from datetime import datetime
from turtle import st

import requests

from model.Session import Session

API_URL = "http://localhost:8080/admin/"  # Example API


def get_sessions():
    response = requests.get(API_URL + "getSessions")

    if response.status_code == 200:
        sessions_data = response.json()

        sessions = []

        for session_data in sessions_data:
            session_date = datetime.strptime(session_data["sessionDate"], "%Y-%m-%d").date()

            time_start = datetime.strptime(session_data["timeStart"], "%H:%M:%S").time()
            time_end = datetime.strptime(session_data["timeEnd"], "%H:%M:%S").time()

            session = Session(
                id=uuid.UUID(session_data["id"]),  # UUID
                name=session_data["name"],
                session_date=session_date,
                time_start=time_start,
                time_end=time_end,
                city=session_data["city"],
                street=session_data["street"],
                building=session_data["building"],
                room_number=session_data["roomNumber"],
                chairman=session_data["chairman"]
            )

            sessions.append(session.to_dict())

        return sessions
    else:
        return []

def get_events():
    response = requests.get(API_URL+"getEventsLectures")
    if response.status_code == 200:
        return response.json()
    else:
        return []