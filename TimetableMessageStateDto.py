class TimetableMessageStateDto:
    def __init__(self, user_id: int, dialog_id: int, message_id: int, group: str, timestamp: float, day: int,
                 week_type: int):
        self.user_id = user_id
        self.dialog_id = dialog_id
        self.message_id = message_id
        self.timestamp = timestamp
        self.day = day
        self.week_type = week_type
        self.group = group

    def __dict__(self):
        return \
            {
                "user_id": self.user_id,
                "dialog_id": self.dialog_id,
                "message_id": self.message_id,
                "timestamp": self.timestamp,
                "day": self.day,
                "week_type": self.week_type,
                "group": self.group
            }
