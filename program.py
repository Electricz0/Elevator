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

def main():

    floors = {}
    for i in range(5):
        floors[str(i)] = i

    elev = elevator.Elevator()

    btns = { "U,{}".format(str(f)) : call_button.CallButton(f,elev,'U') for f in floors}
    btns.update({"D,{}".format(str(f)) : call_button.CallButton(f,elev,'D') for f in floors})

    for k,v in btns.items():
        # print("'{}':{}\n".format(k, str(v)), end='')
        v.press()

    print(elev.call_queue)
main()
