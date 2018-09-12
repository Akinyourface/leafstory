from Globals import *

class GameStateManager:
    def __init__(self):
        self.currentState = ""
    def set_state(self, state):
        self.currentState = state
