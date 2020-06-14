"""
Possible names?
PyLift
LiftLib
ElevatorLib
Elevate
Lev8r


lift/elevator should know what?
    what buttons have been pressed?
    are the doors open?
    what floor/level is it on?
    what direction is it moving?
    is it on or off (general state)?

one bank of lifts should share behavior?
    banks can be subsets of themselves?
    one bank of elevators should share a queue of elevator calls


floor
    up and down buttons?
    method calls will trigger buttons
    send button push calls to corresponding bank of elevators

call object (floor)
    floor number
    direction (optional)

an elevator should inherit from a bank, but with extra features
this way an elevator can act as its own bank if it is used by itself
    call buttons
    door state
    floor state

how to determine buttons:
    a bank, when instatiated, should know the names of all of the floors
        and their order, bottom to top
    floor names/ids should be unique
    elevators inside of a bank can only access floors 
"""

import heapq
from enum import Enum
import time
import threading
import math

def def_call_priority(e,c):
    """
    represents the default priority function
    list of calls
    """
    e_dir = self.direction
    c_dir = c.direction
    same_dir = e_dir == c_dir
    distance = abs( self.floor - c.floor )

    otw = (c.floor >= self.floor) if (e_dir == 'UP') else (c.floor <= self.floor)

    if e_dir is None:
        return distance
    elif same_dir:
        if otw:
            return distance
        else:
            return math.inf
    else:
        return math.inf


class Floor():
    """
    Floor
    """
    def __init__(self, number, name=None):
        self.number = number
        self.name = name or str(self.number)

class Caller():
    """
    Call buttons. Intersects a floor and a bank of elevators
    """

    def __init__(self, floor, bank):
        self.bank = bank
        self.floor = floor
        self.active = True
        self.up = False
        self.down = False
        
    
    def call_up(self):
        self.bank.addCall()
        pass
    
    def call_down(self):
        pass

class Call():
    """
    Request for an elevator
    """
    def __init__(self, floor, direction=None):
        self.time = time.perf_counter()
        self.direction = direction
        self.floor = floor

    def __str__(self):
        return "Call({} @ {})".format(self.direction,self.floor)




def main():
    bank = Bank()
    elevs = [
        Elevator(floor=1,direction=None),
        Elevator(floor=10,direction='DOWN'),
        Elevator(floor=7, direction='UP'),
        Elevator()
    ]

    for e in elevs:
        bank.add_elevator(e)

    print(bank.elevators[0].bank)
    calls = [
        Call(0,'UP'),
        Call(4,'DOWN'),
        Call(-5,'DOWN'),
        Call(-2,'DOWN'),
        Call(8,'UP'),
        Call(7,'UP'),
        Call(8,'DOWN')
    ]

    for c in calls:
        bank.add_call(c)

    bank.update()

    print(bank)

main()
