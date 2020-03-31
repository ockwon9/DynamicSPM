from enum import Enum

class Protocol(Enum):
    EMERGENCY_CHANGE = 1
    IDLE_AND_CHANGE = 2
    FILL_AND_CHANGE = 3
    REDUCED_TRASIENT_PHASE_CHANGE = 4
    FAST_MODE_CHANGE = 5

class Mode:
    def __init__(self, id, name, protocol, applications):
        self.id = id
        self.name = name
        self.protocol = protocol
        self.applications = applications

    def get_partition_size(self, application_id):
        return self.applications[application_id].allocated_partition_size

    def set_partition_size(self, application_id, partition_size):
        self.applications[application_id].allocated_partition_size = partition_size

    def get_max_yipsilon(self):
        max = 0
        for application in self.applications:
            if application.get_yipsilon() <= max:
                max = application.get_yipsilon()
        return max