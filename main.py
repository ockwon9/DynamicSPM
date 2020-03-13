import random
from mode import Mode, Protocol
from task import Task
from application import Application

modes = []

def init():
    t1_1 = Task(1, random.randrange(0, 5), random.randrange(3, 10))
    t1_2 = Task(2, random.randrange(0, 5), random.randrange(3, 10))
    t1_3 = Task(3, random.randrange(0, 5), random.randrange(3, 10))
    t1_4 = Task(4, random.randrange(0, 5), random.randrange(3, 10))
    a1_1 = Application('a1_1', [t1_1, t1_2])
    a1_2 = Application('a1_2', [t1_3, t1_4])
    applications = [a1_1, a1_2]
    modes.append(Mode(1, 'A', Protocol.EMERGENCY_CHANGE, applications))

    t2_1 = Task(5, random.randrange(0, 5), random.randrange(3, 10))
    t2_2 = Task(6, random.randrange(0, 5), random.randrange(3, 10))
    t2_3 = Task(7, random.randrange(0, 5), random.randrange(3, 10))
    t2_4 = Task(8, random.randrange(0, 5), random.randrange(3, 10))
    a2_1 = Application('a2_1', [t2_1, t2_2])
    a2_2 = Application('a2_2', [t2_3, t2_4])
    applications = [a2_1, a2_2]
    modes.append(Mode(2, 'B', Protocol.EMERGENCY_CHANGE, applications))

    t3_1 = Task(9, random.randrange(0, 5), random.randrange(3, 10))
    t3_2 = Task(10, random.randrange(0, 5), random.randrange(3, 10))
    t3_3 = Task(11, random.randrange(0, 5), random.randrange(3, 10))
    t3_4 = Task(12, random.randrange(0, 5), random.randrange(3, 10))
    a3_1 = Application('a3_1', [t3_1, t3_2])
    a3_2 = Application('a3_2', [t3_3, t3_4])
    applications = [a2_1, a2_2]
    modes.append(Mode(3, 'C', Protocol.EMERGENCY_CHANGE, applications))

def allocate_partitions(mode):
    return None

def print_result():
    for mode in modes:
        print('mode %d. %s' % (mode.id, mode.name))
        print('partition: ')
        for partition in mode.partitions:
            print('| %d' % (partition), end='')
        print('\n')

init()
for mode in modes:
    allocate_partitions(mode)
print_result()






