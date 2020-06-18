from threading import Thread
import time
import operator
import math
import call
from direction import Direction

def def_call_priority(e,c):
    """
    c- call\n
    represents the default priority function
    list of calls
    """
    if e.direc != None:
        if e.direc != c.direc:
            # if the call is not going in the
            # same direction as the elevator
            # deprioritize it
            return math.inf
    # determine distance to appropriate calls
    loc_e = e.floors.index(e.floor)
    loc_c = e.floors.index(c.floor)
    return abs(loc_e - loc_c)


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
        
        self.floors = floors
        if len(self.floors) == 0:
            raise(Exception())

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

    def answer_call(self):
        self.call_queue.sort(key=self.prioritize)
        return self.call_queue.pop()

    def queue_to_list(self):
        return [str(c) for c in self.call_queue]

    def run(self):
        """
        Elevator run loop
        """

        # temp behavior
        # run until queue is exhausted
        while len(self.call_queue) > 0:

            print(self.queue_to_list())

            # sort queue based on defined priorities
            self.prioritize()
            print(self.queue_to_list())

            # pop task off of the front of queue
            self.task = self.call_queue.pop(0)

            # determine direction of travel
            if self.direc == None:
                loc_c = self.floors.index(self.task.floor)
                loc_e = self.floors.index(self.floor)
                if loc_c > loc_e:
                    self.direc = Direction.UP
                else:
                    self.direc = Direction.DOWN

            print("New task: go to {}".format(self.task.floor))

            # wait a second (minimize spaming queue)
            time.sleep(1)
