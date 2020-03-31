from enum import Enum

class EVENT(Enum):
    LAST_JOB_FINISHED = 1
    FIRST_JOB_RELEASED = 2
    DELAYED_FIRST_JOB_RESUMED = 3

class Event:
    def __init__(self, time, type, application_index, delta = 0):
        self.time = time
        self.type = type
        self.delta = delta
        self.application_index = application_index

