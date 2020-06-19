"""
program.py

Main program file

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
    floor id
    direction (optional)

an elevator should inherit from a bank, but with extra features?
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

import elevator
import call_button
from call import Call
import time
from direction import Direction

def main():

    # lists of floors must be ordered from lowest to highest floor
    # names must be unique
    floors = ('SB','B','L','2','3','4','5','6','7','8','9','10')

    # print(floors)

    elev = elevator.Elevator(floors,floor="9")

    btns = { "{},U".format(str(f)) : call_button.CallButton( f, elev, Direction.UP ) for f in floors}
    btns.update({"{},D".format(str(f)) : call_button.CallButton(f, elev, Direction.DOWN) for f in floors})

    actions = ["3,D","2,D","6,U","2,U"]

    for b in actions:
        btns[b].press()

    elev.start()
main()
