from birthdeath_power_varstep import BirthDeathPowerVarStep
from numpy import mean, std, arange
import matplotlib.pyplot as plt

# set some indices
hits = []
means_hitting_time = []
stds_hitting_time = []

min_x = -1000
max_x = 1000
x_step = 5
x_vals = arange(min_x, max_x, x_step)

iterations = 1000000

for x in x_vals:
    sim = BirthDeathPowerVarStep(x, 0, 0.5, 1)
    sim.nstep(iterations)
    hits.append(len(sim.hitting_times))

    # append the mean hitting time and standard deviation of hitting time
    # we have to first check if the list is empty, because if it is we will
    # assume the hitting time is the max possible.
    if(len(sim.hitting_times) != 0):
        cur_mean = mean(sim.hitting_times)
        cur_std = std(sim.hitting_times)
        means_hitting_time.append(cur_mean)
        stds_hitting_time.append(cur_std)
    else:
        means_hitting_time.append(iterations)
        stds_hitting_time.append(iterations)

# do some plotting
n_bins = 40
plt.figure(1)
plt.plot(x_vals, means_hitting_time, 'ro-')
plt.xlabel('initial position')
plt.ylabel('mean hitting time')
plt.suptitle('mean hitting time to 0 from a given initial position')

plt.figure(2)
plt.plot(x_vals, stds_hitting_time, 'bo-')
plt.xlabel('initial position')
plt.ylabel('std of hitting time')
plt.suptitle('std of hitting time to 0 from a given initial position')

plt.figure(3)
plt.hist2d(x_vals, means_hitting_time, bins = n_bins)
plt.xlabel('initial position')
plt.ylabel('mean hitting time')
plt.colorbar()
plt.suptitle('mean hitting time to 0 from a given initial position (2d Histogram, %d bins)' % n_bins)

plt.show()
