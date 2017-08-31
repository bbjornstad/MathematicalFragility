# implements a base object representing a random walk simulation.
# in particular, simulations must be derived from this random
# walk simulation in order to implement the step function.
class RandomWalk:
    # initialize some basic variables shared by all random walks
    def __init__(self, init_pos, init_time):
        self.curpos = init_pos
        self.init_pos = init_pos
        self.timestep = init_time
        self.poslist = [init_pos]
        self.hitting_times = []

    # note: this function must be implemented via a derived class.
    # if it is not, an error will be raised.
    # the derived class needs to update the curpos, timestep,
    # poslist, and return_times variables of the RandomWalk
    def _step(self):
        raise NotImplementedError()

    # step n times
    # further checks conditions and updates values as necessary
    # if we reach 0, we return to the initial position and start again.
    def nstep(self, n):
        interval_steps = 0
        for i in range(n):
            self._step()
            interval_steps += 1
            # we have recurred, so record the amount of time it took
            # to do so in the return_times list, and then return to
            # the initial position.
            if(self.poslist[-1] <= 0):
                self.hitting_times.append(interval_steps)
                interval_steps = 0
                self.curpos = self.init_pos
