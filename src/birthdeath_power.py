from randomwalk import RandomWalk
from numpy import random, sqrt, power

class BirthDeathPower(RandomWalk):
    def __init__(self, init_pos, init_time, power):
        super().__init__(init_pos, init_time)
        self.power = power

    def step(self):
        if(random.random() <= self.forward_prob):
            self.curpos += 1
        else:
            self.curpos -= 1

        # update the time step and add the position to the poslist
        self.timestep += 1
        self.poslist.append(self.curpos)

    @property
    def forward_prob(self):
        alpha = 1 / (2 + power((1 + abs(self.curpos)), -self.power))
        if(self.curpos >= 0):
            return alpha
        else:
            return (1 - alpha)
