"""
Call Button class
"""
import call

class CallButton:
    def __init__(self,floor,elev,direc):
        self.floor = floor
        self.elev = elev
        self.direc = direc

    def press(self):
        """
        if pressed, add call with own parameters to elevator call queue
        """
        self.elev.add_call(call.Call(button=self))

    def __str__(self):
        return "CallButton({} @ {} for {})".format(self.direc,self.floor, str(self.elev))