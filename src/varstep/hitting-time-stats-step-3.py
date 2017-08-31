import sys
sys.path.insert(0,'..')

from birthdeath_power_varstep import BirthDeathPowerVarStep
from numpy import mean, std, arange, save
import matplotlib.pyplot as plt

# set some indices
hits = []
means_hitting_time = []
stds_hitting_time = []

param = 0.05

min_step_size = 1
max_step_size = 2000
step_size_increment = 1
step_sizes = arange(min_step_size, max_step_size, step_size_increment)
save('data/step_sizes_{0}'.format(param), step_sizes)

iterations = 10000000

# set some plotting settings
n_bins = 50
label_fontsize = 16
title_fontsize = 20

for s in step_sizes:
    sim = BirthDeathPowerVarStep(0, 0, param, s)
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

# save the data
save('data/means_{0}_from_0'.format(param), means_hitting_time)
save('data/stds_{0}_from_0'.format(param), stds_hitting_time)

# do some plotting
plt.figure(1)
plt.plot(step_sizes, means_hitting_time, 'ro-')
plt.xlabel('Step size', fontsize=label_fontsize)
plt.ylabel('Mean hitting time', fontsize=label_fontsize)
plt.suptitle('Mean hitting time to 0 from 0 given a step size (parameter {0})'.format(param),
        fontsize=title_fontsize)

plt.figure(2)
plt.plot(step_sizes, stds_hitting_time, 'bo-')
plt.xlabel('step size', fontsize=label_fontsize)
plt.ylabel('std of hitting time', fontsize=label_fontsize)
plt.suptitle('std of hitting time to 0 from 0 given a step size (parameter {0})'.format(param),
        fontsize=title_fontsize)

plt.figure(3)
plt.hist2d(step_sizes, means_hitting_time, bins = n_bins)
plt.xlabel('Step size', fontsize=label_fontsize)
plt.ylabel('Mean hitting time', fontsize=label_fontsize)
plt.colorbar()
plt.suptitle('mean hitting time to 0 from 0 given a step size ({0} bins)'.format(n_bins), 
        fontsize=title_fontsize)

hits = []
means_hitting_time = []
stds_hitting_time = []

for s in step_sizes:
    sim = BirthDeathPowerVarStep(100, 0, param, s)
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

# save the data
save('data/means_{0}_from_100'.format(param), means_hitting_time)
save('data/stds_{0}_from_100'.format(param), stds_hitting_time)

# do some plotting
plt.figure(4)
plt.plot(step_sizes, means_hitting_time, 'ro-')
plt.xlabel('Step size', fontsize=label_fontsize)
plt.ylabel('Mean hitting time', fontsize=label_fontsize)
plt.suptitle('Mean hitting time to 0 from 100 given a step size (parameter {0})'.format(param),
        fontsize=title_fontsize)

plt.figure(5)
plt.plot(step_sizes, stds_hitting_time, 'bo-')
plt.xlabel('step size', fontsize=label_fontsize)
plt.ylabel('std of hitting time', fontsize=label_fontsize)
plt.suptitle('std of hitting time to 0 from 100 given a step size (parameter {0})'.format(param),
        fontsize=title_fontsize)

plt.figure(6)
plt.hist2d(step_sizes, means_hitting_time, bins = n_bins)
plt.xlabel('Step size', fontsize=label_fontsize)
plt.ylabel('Mean hitting time', fontsize=label_fontsize)
plt.colorbar()
plt.suptitle('mean hitting time to 0 from 100 given a step size ({0} bins)'.format(n_bins), 
        fontsize=title_fontsize)

hits = []
means_hitting_time = []
stds_hitting_time = []

for s in step_sizes:
    sim = BirthDeathPowerVarStep(1000, 0, param, s)
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

# save the data
save('data/means_{0}_from_1000'.format(param), means_hitting_time)
save('data/stds_{0}_from_1000'.format(param), stds_hitting_time)

# do some plotting
plt.figure(7)
plt.plot(step_sizes, means_hitting_time, 'ro-')
plt.xlabel('Step size', fontsize=label_fontsize)
plt.ylabel('Mean hitting time', fontsize=label_fontsize)
plt.suptitle('Mean hitting time to 0 from 1000 given a step size (parameter {0})'.format(param),
        fontsize=title_fontsize)

plt.figure(8)
plt.plot(step_sizes, stds_hitting_time, 'bo-')
plt.xlabel('step size', fontsize=label_fontsize)
plt.ylabel('std of hitting time', fontsize=label_fontsize)
plt.suptitle('std of hitting time to 0 from 1000 given a step size (parameter {0})'.format(param),
        fontsize=title_fontsize)

plt.figure(9)
plt.hist2d(step_sizes, means_hitting_time, bins = n_bins)
plt.xlabel('Step size', fontsize=label_fontsize)
plt.ylabel('Mean hitting time', fontsize=label_fontsize)
plt.colorbar()
plt.suptitle('mean hitting time to 0 from 1000 given a step size ({0} bins)'.format(n_bins), 
        fontsize=title_fontsize)

plt.show()
