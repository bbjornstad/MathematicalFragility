import sys
sys.path.insert(0,'..')

from birthdeath_power_varstep import BirthDeathPowerVarStep
from numpy import mean, std, arange, save

# set some indices
means_hitting_time = []
stds_hitting_time = []

min_step_size = 1
max_step_size = 100
step_size_increment = 1
step_sizes = arange(min_step_size, max_step_size, step_size_increment)
save('data/step_sizes', step_sizes)

max_beta = 2
beta_step = 0.2
beta_vals = arange(beta_step, max_beta, beta_step)
save('data/beta_vals', beta_vals)

iterations = 100000
init_pos = 1000

for beta in beta_vals:
    cur_means = []
    cur_stds = []
    for s in step_sizes:
        sim = BirthDeathPowerVarStep(init_pos, 0, beta, s)
        sim.nstep(iterations)

        # append the data to the appropriate array
        # we must first check if we have reached the point of interest at all
        if(len(sim.hitting_times) != 0):
            temp_mean = mean(sim.hitting_times)
            temp_std = std(sim.hitting_times)
            cur_means.append(temp_mean)
            cur_stds.append(temp_std)
        else:
            cur_means.append(iterations)
            cur_stds.append(iterations)
    means_hitting_time.append(cur_means)
    stds_hitting_time.append(cur_stds)


# save the data
save('data/means_from_{0}'.format(init_pos), means_hitting_time)
save('data/stds_from_{0}'.format(init_pos), stds_hitting_time)
