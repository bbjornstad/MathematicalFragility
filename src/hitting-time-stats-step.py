from birthdeath_power_varstep import BirthDeathPowerVarStep
from numpy import mean, std, arange
import matplotlib.pyplot as plt

# set some indices
hits = []
means_hitting_time = []
stds_hitting_time = []

min_step_size = 0
max_step_size = 100
step_size_increment = 5
step_sizes = arange(min_step_size, max_step_size, step_size_increment)

iterations = 1000000

for s in step_sizes:
    sim = BirthDeathPowerVarStep(0, 0, 0.5, s)
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
plt.plot(step_sizes, means_hitting_time, 'ro-')
plt.xlabel('step size')
plt.ylabel('mean hitting time')
plt.suptitle('mean hitting time to 0 from 0 given a step size')

plt.figure(2)
plt.plot(step_sizes, stds_hitting_time, 'bo-')
plt.xlabel('step size')
plt.ylabel('std of hitting time')
plt.suptitle('std of hitting time to 0 from 0 given a step size')

plt.figure(3)
plt.hist2d(step_sizes, means_hitting_time, bins = n_bins)
plt.xlabel('step size')
plt.ylabel('mean hitting time')
plt.colorbar()
plt.suptitle('mean hitting time to 0 from 0 given a step size (2d Histogram, %d bins)' % n_bins)

hits = []
means_hitting_time = []
stds_hitting_time = []

for s in step_sizes:
    sim = BirthDeathPowerVarStep(100, 0, 0.5, s)
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
plt.figure(4)
plt.plot(step_sizes, means_hitting_time, 'ro-')
plt.xlabel('step size')
plt.ylabel('mean hitting time')
plt.suptitle('mean hitting time to 0 from 100 given a step size')

plt.figure(5)
plt.plot(step_sizes, stds_hitting_time, 'bo-')
plt.xlabel('step size')
plt.ylabel('std of hitting time')
plt.suptitle('std of hitting time to 0 from 100 given a step size')

plt.figure(6)
plt.hist2d(step_sizes, means_hitting_time, bins = n_bins)
plt.xlabel('step size')
plt.ylabel('mean hitting time')
plt.colorbar()
plt.suptitle('mean hitting time to 0 from 100 given a step size (2d Histogram, %d bins)' % n_bins)

hits = []
means_hitting_time = []
stds_hitting_time = []

for s in step_sizes:
    sim = BirthDeathPowerVarStep(1000, 0, 0.5, s)
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
plt.figure(7)
plt.plot(step_sizes, means_hitting_time, 'ro-')
plt.xlabel('step size')
plt.ylabel('mean hitting time')
plt.suptitle('mean hitting time to 0 from 1000 given a step size')

plt.figure(8)
plt.plot(step_sizes, stds_hitting_time, 'bo-')
plt.xlabel('step size')
plt.ylabel('std of hitting time')
plt.suptitle('std of hitting time to 0 from 1000 given a step size')

plt.figure(9)
plt.hist2d(step_sizes, means_hitting_time, bins = n_bins)
plt.xlabel('step size')
plt.ylabel('mean hitting time')
plt.colorbar()
plt.suptitle('mean hitting time to 0 from 1000 given a step size (2d Histogram, %d bins)' % n_bins)

plt.show()
