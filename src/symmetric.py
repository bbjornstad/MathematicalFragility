from randomwalk import RandomWalk
from numpy import random

class Symmetric(RandomWalk):
    def __init__(self, init_pos, init_time):
        super().__init__(init_pos, init_time)

    def step(self):
        if (random.random() <= 0.5):
            self.curpos -= 1
        else:
            self.curpos += 1

        self.timestep += 1
        self.poslist.append(self.curpos)


# start the simulation from 0 and try a bunch of iterations
sim = Symmetric(0, 0)
sim.nstep(1000000)
print(sim.get_poslist().count(0))
