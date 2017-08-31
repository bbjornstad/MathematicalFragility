from birthdeath_power_varstep import BirthDeathPowerVarStep
from numpy import mean, std, arange
import matplotlib.pyplot as plt

# set some indices
recurrences = []
# holds the mean return times by
mean_return_times = []
std_return_times = []

# make a range of step sizes
min_step_size = 1
max_step_size = 100
step_sizes = arange(min_step_size, max_step_size, 5)

iterations = 1000000

for step_size in step_sizes:
    sim = BirthDeathPowerVarStep(0,0,0.5,step_size)
    sim.nstep(1000000)
    recurrences.append(sim.num_recurrences)
    # append the mean return time and standard deviation of return times
    # we first need to check if the list is empty or not, if it is we
    # must handle the scenario in which the walk did not recur.
    if(len(sim.hitting_times) != 0):
        cur_mean = mean(sim.hitting_times)
        cur_std = std(sim.hitting_times)
        mean_return_times.append(cur_mean)
        std_return_times.append(cur_std)
    else:
        # in this case, the walk never recurred
        mean_return_times.append(iterations)
        std_return_times.append(iterations)

# do some plotting
n_bins = 20
plt.figure(1)
plt.plot(step_sizes, mean_return_times, 'ro-')
plt.xlabel('step size')
plt.ylabel('mean hitting time to 0')
plt.suptitle('mean hitting time vs choice of step size')

plt.figure(2)
plt.plot(step_sizes, std_return_times, 'bo-')
plt.xlabel('step size')
plt.ylabel('std of hitting time')
plt.suptitle('std of hitting time vs choice of step size')

plt.figure(3)
plt.hist(mean_return_times, bins = n_bins, normed=False)
plt.xlabel('mean hitting time')
plt.ylabel('number of step sizes')
plt.suptitle('mean hitting time histogram (%d bins)' % n_bins)

plt.figure(4)
plt.hist2d(step_sizes, mean_return_times, bins = n_bins)
plt.xlabel('step sizes')
plt.ylabel('mean hitting time')
plt.colorbar()
plt.suptitle('mean hitting time 2d histogram - vs step sizes (%d bins)' % n_bins)

plt.show()
