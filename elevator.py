"""
elevator.py

Defines elevator class and default behavior
"""

from threading import Thread
import time
import operator
import math
import call
from direction import Direction

def def_call_priority(e,c):
    """
    e - elevator
    c - call\n
    represents the default priority function
    """
    
    # determine locations of call and elevator
    loc_e = e.floors.index(e.floor)
    loc_c = e.floors.index(c.floor)

    # print("E at {} ord {}\n".format(e.floor,loc_e), end="")
    # print("C at {} ord {}\n".format(c.floor,loc_c), end="")

    # on the way means:
    # floor is in the path of the elevator
    # call is for the same direction the elevator is travelling

    # floor is on the way up
    otwu = e.direc == Direction.UP and loc_c >= loc_e and e.direc == c.direc

    # floor is on the way down
    otwd = e.direc == Direction.DOWN and loc_c <= loc_e and e.direc == c.direc

    # if direction is not set
    # or floor is on the way up or down
    if e.direc == None or otwu or otwd:
        # set priority based on distance to floor
        return abs(loc_e - loc_c)

    # print('lp')

    # otherwise, set lowest priority
    return math.inf


class Elevator(Thread):
    """
    Single elevator object
    """

    def __init__(self, floors, priority=def_call_priority, floor=None, direc=None):
        Thread.__init__(self)
        
        self.call_queue = []
        self.direc = direc
        self.priority = priority
        self.running = True
        self.task = None

        # floors should be defined as a tuple of strings
        # every string should be unique and ordered correctly from
        # lowest floor to highest floor
        # floors must contain at least one floor
        self.floors = floors
        if len(self.floors) == 0:
            raise(Exception())

        # if the starting floor is not defined, start at the lowest floor
        self.floor = floor
        if self.floor == None:
            self.floor = self.floors[0]
    
    def prioritize(self):
        self.call_queue.sort(key=lambda c: self.priority(self,c))

    def __str__(self):
        s = "Elevator({} @ {}: Queue({})".format(self.direc,self.floor,self.queue_to_list())

        return s

    def add_call(self,call):
        self.call_queue.append(call)

    def queue_to_list(self):
        return [str(c) for c in self.call_queue]

    def run(self):
        """
        Elevator run loop
        """

        # temp behavior
        # run until queue is exhausted
        while len(self.call_queue) > 0:
            print(self)

            # print(self.queue_to_list())

            # sort queue based on defined priorities
            self.prioritize()
            # print(self.queue_to_list())

            # pop task off of the front of queue
            self.task = self.call_queue.pop(0)

            # set direction of travel
            # if task is on the way
            # 
            self.direc = self.task.direc
            

            # wait a second (minimize spaming queue)
            # time.sleep(1)
