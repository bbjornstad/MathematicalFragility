from randomwalk import RandomWalk
from numpy import random

# implements a derived Birth and Death simulation from RandomWalk.
# in particular, for a fixed alpha, if the simulation is at a
# coordinate larger than 0, probability to move in the positive
# direction is alpha. otherwise, the probability to move in the
# positive direction is 1-alpha.
class BirthDeath(RandomWalk):
    def __init__(self, init_pos, init_time, alpha):
        super().__init__(init_pos, init_time)
        self.alpha = alpha

    # necessary step function implementation
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
        # if we are past the origin, alpha should be the cutoff
        if(self.curpos >= 0):
            return self.alpha

        # otherwise, 1-alpha should be the cutoff
        else:
            return (1 - self.alpha)


# does some basic steps of the simulation, and prints number of
# recurrences. mostly for debugging purposes
sim = BirthDeath(0, 0, 0.5)
sim.nstep(1000000)
print(sim.poslist.count(0))

sim2 = BirthDeath(0, 0, 0.3)
sim2.nstep(1000000)
print(sim2.poslist.count(0))
