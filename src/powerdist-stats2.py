from birthdeath_power import BirthDeathPower
from numpy import mean, std, arange, matrix
import matplotlib.pyplot as plt

# set some indices
p_recurrences = []
p_means = []
p_stds = []

# make a range of p values
min_p = 0.01
max_p = 2.0
p_step = 0.005
p_vals = arange(min_p, max_p, p_step)



for p in p_vals:
    sim = BirthDeathPower(0,0,p)
    sim.nstep(1000000)
    p_recurrences.append(sim.get_poslist().count(0))
    # compute the mean position and standard deviation of position
    cur_mean = mean(sim.get_poslist())
    cur_std = std(sim.get_poslist())
    p_means.append(cur_mean)
    p_stds.append(cur_std)

# do some plotting
n_bins = 25
plt.figure(1)
plt.plot(p_vals, p_means, 'ro')
plt.plot(p_vals, p_stds, 'bo')
plt.xlabel('p values')
plt.ylabel('mean position and std')
plt.legend(labels=['mean', 'std'])
plt.suptitle('mean and std by p value')

plt.figure(2)
plt.hist(p_means, bins = n_bins, normed=False)
plt.xlabel('mean position')
plt.ylabel('number of p vals')
plt.suptitle('mean position histogram (%d bins)' % n_bins)

plt.figure(3)
plt.hist(p_means, bins = n_bins, normed=False, cumulative=True)
plt.xlabel('mean position')
plt.ylabel('number of p vals (cumulative)')
plt.suptitle('mean position cumulative histogram (%d bins)' % n_bins)

plt.figure(4)
plt.hist2d(p_vals, p_means, bins = n_bins)
plt.xlabel('p vals')
plt.ylabel('mean position')
plt.colorbar()
plt.suptitle('mean position and p-value 2d histogram (%d bins)' % n_bins)

plt.show()
