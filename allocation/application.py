import sys

class Application:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks
        self.allocated_partition_size = 0

    def get_min_partition_size(self):
        return 512;

    def get_longest_execution_time(self):
        max = 0
        for task in self.tasks:
            if task.get_execution_time(self.allocated_partition_size) > max:
                max = task.get_execution_time(self.allocated_partition_size)
        return max

    def get_yipsilon(self):
        min = sys.maxsize
        for task in self.tasks:
            if task.deadline <= min:
                min = task.deadline
        return min