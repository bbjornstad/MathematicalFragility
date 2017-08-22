from randomwalk import RandomWalk
from numpy import random, power

class BirthDeathPowerVarStep(RandomWalk):
    def __init__(self, init_pos, init_time, power, step):
        super().__init__(init_pos, init_time)
        self.power = power
        # here, we implement a variable step size!
        self.stepsize = step

    def _step(self):
        if(random.random() <= self.forward_prob):
            self.curpos += self.stepsize
        else:
            self.curpos -= self.stepsize

        # update the time step and add the position to the poslist
        self.timestep += 1
        self.poslist.append(self.curpos)

    @property
    def forward_prob(self):
        if(self.curpos == 0):
            return (1/2)
        elif(self.curpos > 0):
            alpha = 1 / (2 + power(abs(self.curpos), -self.power))
            return alpha
        else:
            alpha = 1 / (2 + power(abs(self.curpos), -self.power))
            return (1 - alpha)
