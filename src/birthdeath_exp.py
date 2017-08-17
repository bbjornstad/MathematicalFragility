from randomwalk import RandomWalk
from numpy import random, exp

# implements a birth and death chain simulation in which the
# probability of stepping in the positive direction has a
# distribution of alpha = 1 / (2 + exp(-abs(x))) if the current
# position x is larger than 0 and 1 - alpha otherwise.
class BirthDeath(RandomWalk):
    def _step(self):
        if(random.random() <= self.forward_prob):
            self.curpos += 1
        else:
            self.curpos -= 1

        # update the time step and add the position to the poslist
        self.timestep += 1
        self.poslist.append(self.curpos)
        
    @property
    def forward_prob(self):
        alpha = 1 / (2 + exp(-abs(self.curpos)))
        if(self.curpos >= 0):
            return alpha
        else:
            return (1 - alpha)
        

# do some basic simulation work for debugging purposes
sim = BirthDeath(0, 0)
sim.nstep(1000000)
print(sim.get_poslist().count(0))
sim.nstep(1000000)
print(sim.get_poslist().count(0))
sim.nstep(1000000)
print(sim.get_poslist().count(0))
