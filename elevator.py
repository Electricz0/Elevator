class Elevator():
    """
    Single elevator object

    location
    direction
    call_buttons
    queue
    """
    n = 0
    def __init__(self, floor=0, direction=None, bank=None):
        self.call_queue = []
        self.floor = floor
        self.direction = direction
        self.bank = bank
        self.calls = []
        if self.bank:
            self.call_priority = self.bank.call_priority
        else:
            self.call_priority = def_call_priority



    def __str__(self):
        s = "Elevator({} @ {})\n\tCall Queue:\n\t\t".format(self.direction,self.floor)

        s += '\n\t\t'.join([str(c) for c in self.call_queue ])

        return s


    def prioritize(self):
        self.queue.sort(key=self.call_priority)

    def add_call(self,floor):
        self.calls.append(Call(floor))

    def update_queue(self):
        q = self.bank.calls + self.calls

        q.sort(key = self.call_priority)

        self.call_queue = q
