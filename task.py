class Task:
    id = 0
    offset = 0
    min_arrival_time = 0
    deadline = 0

    def __init__(self, id, offset, min_arrival_time):
        self.id = id
        self.offset = offset
        self.min_arrival_time = min_arrival_time
        self.deadline = min_arrival_time

    def get_execution_time(self, size_of_spm):
        return 1