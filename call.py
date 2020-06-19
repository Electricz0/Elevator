"""
call.py

Defines Call class

represents an elevator call

how do i want to represent the prioritization of calls?
    each bank and elevator will have its own way of prioritizing calls
    they can either have their own or inherit from their containing bank
    either it will call its own key function or it will 
"""
from direction import Direction

class Call():
    """
    Request for an elevator
    """

    def __init__(self, button=None, floor=None, direc=None, elev=None):
        if button:
            self.direc = button.direc
            self.floor = button.floor
            self.elev = button.elev
        else:
            self.direc = direc
            self.floor = floor
            self.elev = elev

    def __str__(self):
        return "Call({} @ {})".format(self.direc,self.floor)
    
    def __eq__(self,c):
        pass

    def __lt__(self,c):
        pass

    def __le__(self,c):
        pass

    def __gt__(self,c):
        pass

    def __ge__(self,c):
        pass
