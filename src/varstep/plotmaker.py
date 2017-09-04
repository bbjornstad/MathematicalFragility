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
mean_fig, m_splots = plt.subplots(nrows = 1, ncols = 2, sharex = True, sharey = True, figsize=(16,9))
for i, beta_slice in enumerate(means_hitting_time):
    cur_beta = beta_vals[i]
    if cur_beta < 1:
        m_splots[0].plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
    else:
        m_splots[1].plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
for splot in m_splots:
    # also plot the reference x/s
    splot.plot(step_sizes, reference, '--', label='Reference')
    # make it pretty
    splot.legend(fontsize=legend_fontsize)
    splot.set_xlabel('Step size', fontsize=label_fontsize)
    splot.set_ylabel('Mean hitting time', fontsize=label_fontsize)
    splot.tick_params(axis='both', labelsize=axis_fontsize)
    splot.set_ybound(0,25000)
m_splots[0].set_title(r'$\beta < 1$', fontsize=label_fontsize)
m_splots[1].set_title(r'$\beta \geq 1$', fontsize=label_fontsize)

mean_fig.suptitle('Mean hitting time to 0 from {0} by step size'.format(init_pos),
        fontsize=title_fontsize)


std_fig, s_splots = plt.subplots(nrows = 1, ncols = 2, sharex = True, sharey = True, figsize=(16,9))
for i, beta_slice in enumerate(stds_hitting_time):
    cur_beta = beta_vals[i]
    if cur_beta < 1:
        s_splots[0].plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
    else:
        s_splots[1].plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
for splot in s_splots:
    # also plot the reference x/s
    splot.plot(step_sizes, reference, '--', label='Reference')
    # make it pretty
    splot.legend(fontsize=legend_fontsize)
    splot.set_xlabel('Step size', fontsize=label_fontsize)
    splot.set_ylabel('STD of hitting time', fontsize=label_fontsize)
    splot.tick_params(axis='both', labelsize=axis_fontsize)
    splot.set_ybound(0,25000)
s_splots[0].set_title(r'$\beta < 1$', fontsize=label_fontsize)
s_splots[1].set_title(r'$\beta \geq 1$', fontsize=label_fontsize)

std_fig.suptitle('STD of hitting time to 0 from {0} by step size'.format(init_pos),
        fontsize=title_fontsize)

# save
mean_fig.savefig('plots/from_{0}_means.jpg'.format(init_pos))
std_fig.savefig('plots/from_{0}_stds.jpg'.format(init_pos))
