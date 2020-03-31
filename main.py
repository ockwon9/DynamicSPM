import random
import time
from mode import Mode, Protocol
from task import Task
from application import Application
from event import Event, EVENT

# System Constants
SPM_SIZE = 2048
SPM_ALLOCATION_UNIT = 4

# Global Variables
modes = []

def initialize():
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
    modes.append(Mode(2, 'B', Protocol.IDLE_AND_CHANGE, applications))

    t3_1 = Task(9, random.randrange(0, 5), random.randrange(3, 10))
    t3_2 = Task(10, random.randrange(0, 5), random.randrange(3, 10))
    t3_3 = Task(11, random.randrange(0, 5), random.randrange(3, 10))
    t3_4 = Task(12, random.randrange(0, 5), random.randrange(3, 10))
    a3_1 = Application('a3_1', [t3_1, t3_2])
    a3_2 = Application('a3_2', [t3_3, t3_4])
    applications = [a3_1, a3_2]
    modes.append(Mode(3, 'C', Protocol.FILL_AND_CHANGE, applications))

    t4_1 = Task(13, random.randrange(0, 5), random.randrange(3, 10))
    t4_2 = Task(14, random.randrange(0, 5), random.randrange(3, 10))
    t4_3 = Task(15, random.randrange(0, 5), random.randrange(3, 10))
    t4_4 = Task(16, random.randrange(0, 5), random.randrange(3, 10))
    a4_1 = Application('a4_1', [t4_1, t4_2])
    a4_2 = Application('a4_2', [t4_3, t4_4])
    applications = [a4_1, a4_2]
    modes.append(Mode(4, 'D', Protocol.FAST_MODE_CHANGE, applications))

    t5_1 = Task(17, random.randrange(0, 5), random.randrange(3, 10))
    t5_2 = Task(18, random.randrange(0, 5), random.randrange(3, 10))
    t5_3 = Task(19, random.randrange(0, 5), random.randrange(3, 10))
    t5_4 = Task(10, random.randrange(0, 5), random.randrange(3, 10))
    a5_1 = Application('a5_1', [t5_1, t5_2])
    a5_2 = Application('a5_2', [t5_3, t5_4])
    applications = [a5_1, a5_2]
    modes.append(Mode(5, 'E', Protocol.REDUCED_TRASIENT_PHASE_CHANGE, applications))

def allocate_spm():
    for i in range(len(modes)):
        if i > 0:
            prev_mode = modes[i - 1]
        next_mode = modes[i]
        print("Mode %d: %s" % (i, next_mode.protocol))
        num_of_partitions = len(next_mode.applications)
        remaining_spm_size = SPM_SIZE
        random.seed(i)

        if next_mode.protocol == Protocol.EMERGENCY_CHANGE or \
                next_mode.protocol == Protocol.IDLE_AND_CHANGE or \
                next_mode.protocol == Protocol.FILL_AND_CHANGE:
            for j in range(num_of_partitions):
                min_spm_size = get_min_spm_size(next_mode.applications[j], 0, 0)
                if remaining_spm_size >= min_spm_size:
                    next_mode.partitions.append(min_spm_size)
                    remaining_spm_size = remaining_spm_size - min_spm_size
                else:
                    print("SPM allocation failed in application [%d] on mode [%d]" % (j, i))
            next_mode.reserved_spm_size = remaining_spm_size
        elif next_mode.protocol == Protocol.FAST_MODE_CHANGE:
            # Initialize required variables for the SPM allocation
            remaining_spm_size = prev_mode.reserved_spm_size
            event_list = []
            for processor_index in range(len(prev_mode.applications)):
                 event_list.append(Event(prev_mode.applications[processor_index].get_longest_execution_time(), EVENT.LAST_JOB_FINISHED, processor_index))
                event_list.append(Event(prev_mode.applications[processor_index].get_shortest_period(), EVENT.FIRST_JOB_RELEASED, processor_index))

            # Start the allocation assuming the mode change signal is arrived at t=0
            t = 0
            while event_list:
                event = get_next_event(event_list)
                t = event.time
                if event.type == EVENT.LAST_JOB_FINISHED:
                    remaining_spm_size = remaining_spm_size + prev_mode.partitions[event.processor_index]
                elif event.type == EVENT.FIRST_JOB_RELEASED:
                    min_spm_size = get_min_spm_size(next_mode.applications[event.processor_index], \
                                                    prev_modeapplication.get_shortest_period(), 0)
                    if min_spm_size <= remaining_spm_size:
                        next_mode.partitions[event.processor_index] = min_spm_size
                    else:
                        next_finish_event = get_next_finish_event(event_list)
                        delta = event.delta + (next_finish_event.time - t)
                        event_list.append(Event(next_finish_event.time, EVENT.DELAYED_FIRST_JOB_RESUMED, \
                                                event.processor_index, delta))
                elif event.type == EVENT.DELAYED_FIRST_JOB_RESUMED:
                    t = event.time
                    for ev in event_list:
                        if ev.time <= current_time and ev.type == EVENT.LAST_JOB_FINISHED:
                            event_list.pop(ev)
                            remaining_spm_size = remaining_spm_size + prev_mode.partitions[ev.processor_index]

                    min_spm_size = get_min_spm_size(next_mode.applications[event.processor_index], \
                                                    prev_modeapplication.get_shortest_period(), event.delta)
                    if min_spm_size <= remaining_spm_size:
                        next_mode.partitions[event.processor_index] = min_spm_size
                    else:
                        next_finish_event = get_next_finish_event(event_list)
                        delta = event.delta + (next_finish_event.time - t)
                        event_list.append(Event(next_finish_event.time, EVENT.DELAYED_FIRST_JOB_RESUMED, \
                                                event.processor_index, next_finish_event.time - t))
                else:
                    continue
        elif next_mode.protocol == Protocol.REDUCED_TRASIENT_PHASE_CHANGE:
            continue
    return None

#TODO: Implementation of this function
def is_schedulable(application, epsilon, sigma):
    return False

#TODO: Implementation of this function
def get_min_spm_size(application, epsilon, sigma):
    if is_schedulable(application, epsilon, sigma):
        print("Schedulable!!")
    i = random.random()
    i = int(i * 2048 / 2)
    return i

def print_result():
    print('')
    for mode in modes:
        print('mode %d. %s' % (mode.id, mode.name))
        print('partition: ')
        for partition in mode.partitions:
            print('| %d ' % (partition), end='')
        print('|\n')

# Initialize the system environment
initialize()

# Allocate SPM sequentially for all modes
allocate_spm()

# Print the allocation result
print_result()






