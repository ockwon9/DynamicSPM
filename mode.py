from enum import Enum

class Protocol(Enum):
    EMERGENCY_CHANGE = 1
    IDLE_AND_CHANGE = 2
    FILL_AND_CHANGE = 3
    REDUCED_TRASIENT_PHASE_CHANGE = 4
    FAST_MODE_CHANGE = 5

class Mode:
    id = 0
    name = ''
    protocol = 1
    applications = None
    partitions = []

    def __init__(self, id, name, protocol, applications):
        self.id = id
        self.name = name
        self.protocol = protocol
        self.applications = applications
        self.partitions = []

    def get_partition_size(self, processor_id):
        return self.partitions[processor_id]
