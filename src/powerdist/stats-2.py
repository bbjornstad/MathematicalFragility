from birthdeath_power import BirthDeathPower
from numpy import mean, std, arange
import matplotlib.pyplot as plt

# here, we utilize the BirthDeathPower class (derived from RandomWalk)
# to run a simulation of a birth and death simulation using the
# specified probability distributions. we loop through a range of 
# beta values which will serve as the exponents in the distribution,
# and do statistical analysis on the return times. we then plot the results.

# set some indices
recurrences = []
# holds the mean return times by
mean_return_times = []
std_return_times = []

# make a range of beta values
min_beta = 0.0000
max_beta = 4.0
beta_step = 0.0005
beta_vals = arange(min_beta, max_beta, beta_step)

iterations = 1000000

for beta in beta_vals:
    sim = BirthDeathPower(0,0,beta)
    sim.nstep(iterations)
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
n_bins = 100
plt.figure(1)
plt.plot(beta_vals, mean_return_times, 'ro-')
plt.xlabel('beta values')
plt.ylabel('mean return time')
plt.suptitle('mean return time vs choice of beta')

plt.figure(2)
plt.plot(beta_vals, std_return_times, 'bo-')
plt.xlabel('beta values')
plt.ylabel('std of return time')
plt.suptitle('std of return time vs choice of beta')

plt.figure(3)
plt.hist(mean_return_times, bins = n_bins, normed=False)
plt.xlabel('mean return time')
plt.ylabel('number of beta vals')
plt.suptitle('mean return time histogram (%d bins)' % n_bins)

plt.figure(4)
plt.hist2d(beta_vals, mean_return_times, bins = n_bins)
plt.xlabel('beta vals')
plt.ylabel('mean return time')
plt.colorbar()
plt.suptitle('mean return time 2d histogram - vs beta values (%d bins)' % n_bins)

plt.show()
