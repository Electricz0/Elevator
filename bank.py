import threading
import program
import heapq

class Bank():
    """
    Group of elevators

    can contain banks or elevators
    has a queue of calls made for elevators in the bank
    
    """

    elevators = []

    def __init__(self, call_priority=program.def_call_priority):
        # call queue (should be a priority queue)
        self.call_queue = heapq

        # lock for the queue (only one access at a time to prevent conflicts)
        self.queue_lock = threading.RLock()

        # contained banks and elevators
        self.members = []

    def __iter__(self):
        """
        make bank iterable via its members list
        """
        self.itr = iter(self.members)
        return self.itr

    def __next__(self):
        return next(self.itr)

    def __str__(self):
        s = 'Bank:\n\t'

        s += '\n\t'.join(['Elevator({} @ {}):'.format(e.direction,e.floor) + '\n\t\t' +"\n\t\t".join(['Call({} @ {})'.format(c.direction,c.floor) for c in e.call_queue]) for e in self.elevators])

        return s

    def add_elevator(self,elev):
        elev.bank = self
        self.elevators.append(elev)
    
    def make_call(self,call):
        """
        add call to priority queue
        """
        self.call_queue.append(call)
    
    def update(self):
        for e in self:
            e.update_queue()

# end bank
