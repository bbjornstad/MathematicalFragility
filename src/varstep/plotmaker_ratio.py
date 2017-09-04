from numpy import arange, load
import matplotlib.pyplot as plt

init_pos = 1000
# set some indices
means = load('data/means_from_{0}.npy'.format(init_pos))
stds = load('data/stds_from_{0}.npy'.format(init_pos))
beta_vals = load('data/beta_vals.npy')
step_sizes = load('data/step_sizes.npy')
reference = [1 for s in step_sizes]

# calculate the ratios
means_ratio = map((lambda m, s: m/(init_pos/s)), means, step_sizes)
stds_ratio = map((lambda m, s: m/(init_pos/s)), stds, step_sizes)

# set some plotting settings
title_fontsize = 14
label_fontsize = 12
axis_fontsize = 11
legend_fontsize = 10

# do some plotting
mean_fig, m_splots = plt.subplots(nrows = 1, ncols = 2, sharex = True, sharey = True, figsize=(16,9))
for i, beta_slice in enumerate(means_ratio):
    cur_beta = beta_vals[i]
    if cur_beta < 1:
        m_splots[0].plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
    else:
        m_splots[1].plot(step_sizes, beta_slice, 'o-', label=r'$\beta = {}$'.format(round(cur_beta, 1)))
for splot in m_splots:
    # also plot the reference
    splot.plot(step_sizes, reference, '--', label='Reference')
    # make it pretty
    splot.legend(fontsize=legend_fontsize)
    splot.set_xlabel('Step size', fontsize=label_fontsize)
    splot.set_ylabel('Mean hitting time', fontsize=label_fontsize)
    splot.tick_params(axis='both', labelsize=axis_fontsize)
m_splots[0].set_title(r'$\beta < 1$', fontsize=label_fontsize)
m_splots[1].set_title(r'$\beta \geq 1$', fontsize=label_fontsize)

mean_fig.suptitle(r'Mean hitting time from {0} as a ratio of $x/s$'.format(init_pos),
        fontsize=title_fontsize)


std_fig, s_splots = plt.subplots(nrows = 1, ncols = 2, sharex = True, sharey = True, figsize=(16,9))
for i, beta_slice in enumerate(stds_ratio):
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
s_splots[0].set_title(r'$\beta < 1$', fontsize=label_fontsize)
s_splots[1].set_title(r'$\beta \geq 1$', fontsize=label_fontsize)

std_fig.suptitle(r'STD of hitting time from {0} as a ratio of $x/s$'.format(init_pos),
        fontsize=title_fontsize)

# save
mean_fig.savefig('plots/from_{0}_means_ratio.jpg'.format(init_pos))
std_fig.savefig('plots/stds_from_{0}_stds_ratio.jpg'.format(init_pos))
