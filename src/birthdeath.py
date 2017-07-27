from randomwalk import RandomWalk
from numpy import random

class BirthDeath(RandomWalk):
    def __init__(self, init_pos, init_time, alpha):
        super().__init__(init_pos, init_time)
        self.alpha = alpha

    def step(self):
        if(random.random() <= self.computeForwardProb()):
            self.curpos += 1
        else:
            self.curpos -= 1

        # update the time step and add the position to the poslist
        self.timestep += 1
        self.poslist.append(self.curpos)

    def computeForwardProb(self):
        # if we are past the origin, alpha should be the cutoff
        if(self.curpos >= 0):
            return self.alpha
        # otherwise, 1-alpha should be the cutoff
        else:
            return (1 - self.alpha)


sim = BirthDeath(0, 0, 0.5)
sim.nstep(1000000)
print(sim.get_poslist().count(0))

sim2 = BirthDeath(0, 0, 0.3)
sim2.nstep(1000000)
print(sim2.get_poslist().count(0))
