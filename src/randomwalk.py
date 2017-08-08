class RandomWalk:
    # initialize some basic variables shared by all random walks
    def __init__(self, init_pos, init_time):
        self.curpos = init_pos
        self.timestep = init_time
        self.poslist = []

    def get_poslist(self):
        return self.poslist

    def get_curpos(self):
        return self.curpos

    def get_timestep(self):
        return self.timestep

    def step(self):
        raise NotImplementedError()

    # simply step n times
    def nstep(self, n):
        for i in range(n):
            self.step()
