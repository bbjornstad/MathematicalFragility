from numpy import arange, load
import matplotlib.pyplot as plt

# set parameters here
init_pos = 1000

# set some indices
means_hitting_time = load('data/means_from_{0}.npy'.format(init_pos))
stds_hitting_time = load('data/stds_from_{0}.npy'.format(init_pos))
beta_vals = load('data/beta_vals.npy')
step_sizes = load('data/step_sizes.npy')
reference = [(init_pos/s) for s in step_sizes]

# set some plotting settings
title_fontsize = 14
label_fontsize = 12
axis_fontsize = 11
legend_fontsize = 10
fig_dpi = 199

# do some plotting
mean_fig, m_splot = plt.subplots(nrows = 1, ncols = 1, sharex = True, sharey = True, figsize=(16,9))
for i, beta_slice in enumerate(means_hitting_time):
    cur_beta = beta_vals[i]
    m_splot.plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
# also plot the reference x/s
m_splot.plot(step_sizes, reference, '--', label='Reference')
# make it pretty
m_splot.legend(fontsize=legend_fontsize)
m_splot.set_xlabel('Step size', fontsize=label_fontsize)
m_splot.set_ylabel('Mean hitting time', fontsize=label_fontsize)
m_splot.tick_params(axis='both', labelsize=axis_fontsize)
m_splot.set_ybound(0,3000)

mean_fig.suptitle('Mean hitting time to 0 from {0} by step size'.format(init_pos),
        fontsize=title_fontsize)


std_fig, s_splot = plt.subplots(nrows = 1, ncols = 1, sharex = True, sharey = True, figsize=(16,9))
for i, beta_slice in enumerate(stds_hitting_time):
    cur_beta = beta_vals[i]
    s_splot.plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
# also plot the reference x/s
s_splot.plot(step_sizes, reference, '--', label='Reference')
# make it pretty
s_splot.legend(fontsize=legend_fontsize)
s_splot.set_xlabel('Step size', fontsize=label_fontsize)
s_splot.set_ylabel('STD of hitting time', fontsize=label_fontsize)
s_splot.tick_params(axis='both', labelsize=axis_fontsize)
s_splot.set_ybound(0,3000)

std_fig.suptitle('STD of hitting time to 0 from {0} by step size'.format(init_pos),
        fontsize=title_fontsize)

# save
mean_fig.savefig('plots/from_{0}_means.jpg'.format(init_pos))
std_fig.savefig('plots/from_{0}_stds.jpg'.format(init_pos))
