from randomwalk import RandomWalk
from numpy import random, exp

class BirthDeath(RandomWalk):
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
        alpha = 1 / (2 + exp(-abs(self.curpos)))
        if(self.curpos >= 0):
            return alpha
        else:
            return (1 - alpha)
        


sim = BirthDeath(0, 0)
sim.nstep(1000000)
print(sim.get_poslist().count(0))
sim.nstep(1000000)
print(sim.get_poslist().count(0))
sim.nstep(1000000)
print(sim.get_poslist().count(0))
