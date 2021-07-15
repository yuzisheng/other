import matplotlib.pyplot as plt

font_size = 36
marker_size = 16
color = ['#60acfc', '#32d3eb', '#5bc49f', '#feb64d', '#ff7c7c']

budgets = [i + 1 for i in range(7)]
karate_budget_1to7 = [0, 0.15, 0.29, 0.4, 0.7, 0.78, 0.82]
dol_budget_1to7 = [0, 0.12, 0.12, 0.23, 0.34, 0.43, 0.52]
lesm_budget_1to7 = [0.12, 0.24, 0.22, 0.35, 0.35, 0.77, 0.87]
pol_budget_1to7 = [0, 0.06, 0.11, 0.23, 0.19, 0.24, 0.37]
footb_budget_1to7 = [0.11, 0.22, 0.32, 0.58, 0.4, 0.78, 0.73]

conv_rate = [0, 5, 10, 15, 20, 25, 30]
karate_conv_0to30 = [4, 3, 3, 3, 0, 0, 0]
dol_conv_0to30 = [3, 3, 3, 1, 1, 1, 0]
lesm_conv_0to30 = [2, 2, 1, 0, 0, 0, 0]
pol_conv_0to30 = [3, 3, 3, 1, 1, 0, 0]
footb_conv_0to30 = [3, 3, 2, 2, 2, 1, 0]

weight = [0, 0.3, 0.5, 0.7, 1.0]
karate_weight_0to1 = [0.35, 0.37, 0.74, 0.47, 0.13]
dol_weight_0to1 = [0.12, 0.22, 0.43, 0.44, 0.11]
lesm_weight_0to1 = [0.34, 0.40, 0.58, 0.52, 0.11]
pol_weight_0to1 = [0.12, 0.18, 0.19, 0.21, 0]
footb_weight_0to1 = [0.06, 0.1, 0.12, 0, 0]

budgets_for_time = [1, 2, 3, 4, 5, 6]
kara_time_random = [0.015, 0.015, 0.015, 0.017, 0.017, 0.018]
kara_time_greedy = [0.02, 0.021, 0.024, 0.028, 0.029, 0.033]
kara_time_genetic = [1, 1, 1, 1, 1, 1]
kara_time_brute_force = [0.02, 0.06, 0.64, 6.34, 54.31, 416.18]
kara_time_sim_ann = [0.02, 0.11, 0.86, 4.49, 16.4, 45.02]


def plot_diff_budget():
    plt.figure(figsize=(4.05, 4.05))
    plt.plot(budgets, karate_budget_1to7, marker='s', label='Kara', markersize=8)
    plt.plot(budgets, dol_budget_1to7, marker='o', label='Dol', markersize=8)
    plt.plot(budgets, lesm_budget_1to7, marker='^', label='Lesm', markersize=8)
    plt.plot(budgets, pol_budget_1to7, marker='*', label='Pol', markersize=8)
    plt.plot(budgets, footb_budget_1to7, marker='v', label='Footb', markersize=8)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$\\beta$", fontsize=20)
    plt.ylabel("$\mathcal{H}$", fontsize=20)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../data/zisheng-icjai-2020/diff_budget.pdf")
    plt.show()


def plot_diff_conv_rate():
    plt.figure(figsize=(4.05, 4.05))
    plt.plot(conv_rate, karate_conv_0to30, marker='s', label='Kara', markersize=8)
    plt.plot(conv_rate, dol_conv_0to30, marker='o', label='Dol', markersize=8)
    plt.plot(conv_rate, lesm_conv_0to30, marker='^', label='Lesm', markersize=8)
    plt.plot(conv_rate, pol_conv_0to30, marker='*', label='Pol', markersize=8)
    plt.plot(conv_rate, footb_conv_0to30, marker='v', label='Footb', markersize=8)
    plt.legend()
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim(-0.3, 4.3)  # just present int number in y-axis
    plt.xlabel("$\\lambda$", fontsize=20)
    plt.ylabel("$|E^{-}|$", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/zisheng-icjai-2020/diff_conv_rate.pdf")
    plt.show()


def plot_diff_weight():
    plt.figure(figsize=(4.05, 4.05))
    plt.plot(weight, karate_weight_0to1, marker='s', label='Kara', markersize=8)
    plt.plot(weight, dol_weight_0to1, marker='o', label='Dol', markersize=8)
    plt.plot(weight, lesm_weight_0to1, marker='^', label='Lesm', markersize=8)
    plt.plot(weight, pol_weight_0to1, marker='*', label='Pol', markersize=8)
    plt.plot(weight, footb_weight_0to1, marker='v', label='Footb', markersize=8)
    plt.legend(loc='best')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xlabel("$w$", fontsize=20)
    plt.ylabel("$\mathcal{H}}$", fontsize=20)
    plt.tight_layout()
    plt.savefig("../data/zisheng-icjai-2020/diff_weight.pdf")
    plt.show()


def plot_all():
    # plt.figure(figsize=(13, 4))

    plt.subplot(131)
    plt.plot(budgets, karate_budget_1to7, marker='s', label='Kara', markersize=marker_size, color=color[0])
    plt.plot(budgets, dol_budget_1to7, marker='o', label='Dol', markersize=marker_size, color=color[1])
    plt.plot(budgets, lesm_budget_1to7, marker='^', label='Lesm', markersize=marker_size, color=color[2])
    plt.plot(budgets, pol_budget_1to7, marker='*', label='Pol', markersize=marker_size, color=color[3])
    plt.plot(budgets, footb_budget_1to7, marker='v', label='Footb', markersize=marker_size, color=color[4])
    plt.legend(fontsize=20)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.xlabel("$\\beta$\n(a) $\mathcal{H}$ with different $\\beta$", fontsize=font_size)
    plt.ylabel("$\mathcal{H}$", fontsize=font_size)

    plt.subplot(132)
    plt.plot(conv_rate, karate_conv_0to30, marker='s', label='Kara', markersize=marker_size, color=color[0])
    plt.plot(conv_rate, dol_conv_0to30, marker='o', label='Dol', markersize=marker_size, color=color[1])
    plt.plot(conv_rate, lesm_conv_0to30, marker='^', label='Lesm', markersize=marker_size, color=color[2])
    plt.plot(conv_rate, pol_conv_0to30, marker='*', label='Pol', markersize=marker_size, color=color[3])
    plt.plot(conv_rate, footb_conv_0to30, marker='v', label='Footb', markersize=marker_size, color=color[4])
    # plt.legend(fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.ylim(-0.3, 4.3)  # just present int number in y-axis
    plt.xlabel("$\\lambda$\n(b) $|E^{-}|$ with different $\\lambda$", fontsize=font_size)
    plt.ylabel("$|E^{-}|$", fontsize=font_size)

    plt.subplot(133)
    plt.plot(weight, karate_weight_0to1, marker='s', label='Kara', markersize=marker_size, color=color[0])
    plt.plot(weight, dol_weight_0to1, marker='o', label='Dol', markersize=marker_size, color=color[1])
    plt.plot(weight, lesm_weight_0to1, marker='^', label='Lesm', markersize=marker_size, color=color[2])
    plt.plot(weight, pol_weight_0to1, marker='*', label='Pol', markersize=marker_size, color=color[3])
    plt.plot(weight, footb_weight_0to1, marker='v', label='Footb', markersize=marker_size, color=color[4])
    # plt.legend(loc='best', fontsize=font_size)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.xlabel("$\\omega$\n(c) $\mathcal{H}}$ with different $\\omega$", fontsize=font_size)
    plt.ylabel("$\mathcal{H}}$", fontsize=font_size)

    # plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # plot_diff_budget()
    # plot_diff_conv_rate()
    # plot_diff_weight()
    plot_all()

    print("ok")
