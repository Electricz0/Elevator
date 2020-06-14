from collections import OrderedDict
from threading import Thread

def def_call_priority(e,c):
    """
    c- call\n
    represents the default priority function
    list of calls
    """
    
    return 0

class Elevator(Thread):
    """
    Single elevator object
    """

    def __init__(self, prioritize=def_call_priority,floors=[], floor=0, direc=None, bank=None):
        Thread.__init__(self)
        self.call_queue = []
        self.floor = floor
        self.direc = direc
        self.prioritize = prioritize
        self.running = True
        
    def __str__(self):
        s = "Elevator({} @ {})".format(self.direc,self.floor)

        # s += '\n\t\t'.join([str(c) for c in self.call_queue ])

        return s

    def add_call(self,call):
        self.call_queue.append(call)

    def answer_call(self):
        self.call_queue.sort(key=self.prioritize)
        return self.call_queue.pop()

    def run(self):
        while self.running:
            print('running\n',end='')
