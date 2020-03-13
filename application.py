class Application:
    name = ''
    tasks = None

    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def get_min_partition_size(self):
        return 512;