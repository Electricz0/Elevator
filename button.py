"""
Button classes

"""
import call

class Button():
    def __init__(self,floor,elev):
        self.floor = floor
        self.eleve = elev
    
    def press(self):
        self.elev.add_call(call.Call(button=self))

    def __str__(self):
        return "CallButton({} @ {} for {})".format(self.direc,self.floor, str(self.elev))

class ElevatorButton(Button):
    def __init__(self,floor,elev):
        Button.__init__(self,floor,elev)

class CallButton(Button):
    def __init__(self,floor,elev,direc):
        Button.__init__(self,floor,elev)
        self.direc = direc


