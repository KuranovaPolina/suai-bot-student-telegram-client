from typing import Optional

from pymongo import MongoClient

import TimetableMessageStateDto
from TimetableMessageStateDto import TimetableMessageStateDto


class TimetableMessageStatesMongoClient:
    def __init__(self, connection_string: str):
        self.client = MongoClient(connection_string)
        self.states = self.client['suai-tg-bot']['timetable_message_states']

    def disconnect(self):
        self.client.close()

    def get_state(self, dialog_id, message_id) -> Optional[TimetableMessageStateDto]:
        states = self.states.find(
            filter=
            {
                "dialog_id": dialog_id,
                "message_id": message_id,
            }).sort('timestamp', -1)

        try:
            state = states[0]
            return TimetableMessageStateDto(
                dialog_id=state['dialog_id'],
                message_id=state['message_id'],
                user_id=state['user_id'],
                day=state['day'],
                week_type=state['week_type'],
                group=state['group'],
                timestamp=state['timestamp']
            )
        except Exception:
            return None

    def add_state(self, state: TimetableMessageStateDto):
        self.states.insert_one(state.to_dict())
