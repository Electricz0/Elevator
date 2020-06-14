"""
CallCollector class

elevators and banks both inherit from this class
implements the call collection and call prioritization behaviors
"""
def def_call_priority(e,c):
    """
    c- call\n
    represents the default priority function
    list of calls
    """
    return 0

class CallCollector:
    def __init__(self, priority=def_call_priority):
        self.queue = []
        self.priority = priority
