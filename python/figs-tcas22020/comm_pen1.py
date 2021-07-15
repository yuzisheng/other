import matplotlib.pyplot as plt
import numpy as np

dataset = ['kara', 'dol', 'lesm', 'polb', 'footb', 'faceb']
x, width = np.arange(len(dataset)), 0.9 / len(dataset)
# color = ['c', 'g', 'b', 'r', 'y']
color = ['#60acfc', '#32d3eb', '#5bc49f', '#feb64d', '#ff7c7c']
font_size = 18

fig = plt.figure()
plt.ylim(0, 1)

# Figure 1
ax1 = plt.subplot(2, 3, 1)
plt.ylim(0, 1)
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
# eig_tree_kara = [0.13, 0.36, 0.48, 0.82, 0.48]
# eig_tree_dol = [0.37, 0.71, 0.37, 0.84, 0.37]
# eig_tree_lesm = [0.37, 0.42, 0.41, 0.50, 0.52]
# eig_tree_polb = [0.43, 0.81, 0.74, 0.84, 0.63]
# eig_tree_footb = [0.54, 0.72, 0.84, 0.88, 0.83]
# eig_tree_faceb = [0.95, 0.97, 0.98, 0.97, 0.71]

eig_tree_rs = [0.13, 0.37, 0.37, 0.43, 0.54, 0.95]
eig_tree_ga = [0.36, 0.71, 0.42, 0.81, 0.72, 0.97]
eig_tree_gs = [0.48, 0.37, 0.41, 0.74, 0.84, 0.98]
eig_tree_msa = [0.82, 0.84, 0.5, 0.84, 0.88, 0.97]
eig_tree_bf = [0.48, 0.37, 0.52, 0.63, 0.83, 0.71]

plt.bar(x, eig_tree_rs, width=width, label='RS', fc=color[0])
plt.bar(x + width, eig_tree_ga, width=width, label='GA', fc=color[1])
plt.bar(x + 2 * width, eig_tree_gs, width=width, label='GS', fc=color[2], tick_label=dataset)
plt.bar(x + 3 * width, eig_tree_msa, width=width, label='MSA', fc=color[3])
plt.bar(x + 4 * width, eig_tree_bf, width=width, label='BF', fc=color[4])
plt.legend(ncol=5)
plt.xlabel("(a) Tree graph attack against EIG detection", fontsize=font_size)
plt.ylabel("$\mathcal{P}$", fontsize=font_size)

# Figure 2
ax2 = plt.subplot(2, 3, 2)
plt.ylim(0, 1)
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
# eig_complete_kara = [0.22, 0.23, 0.23, 0.40, 0.23]
# eig_complete_dol = [0.47, 0.87, 0.23, 0.93, 0.00]
# eig_complete_lesm = [0.37, 0.55, 0.38, 0.56, 0.48]
# eig_complete_polb = [0.38, 0.65, 0.82, 0.93, 0.93]
# eig_complete_footb = [0.64, 0.80, 0.74, 0.83, 0.92]
# eig_complete_faceb = [0.11, 0.16, 0.42, 0.65, 0.50]

eig_complete_rs = [0.22, 0.47, 0.37, 0.38, 0.64, 0.11]
eig_complete_ga = [0.23, 0.87, 0.55, 0.65, 0.8, 0.16]
eig_complete_gs = [0.23, 0.23, 0.38, 0.82, 0.74, 0.42]
eig_complete_msa = [0.4, 0.93, 0.56, 0.93, 0.83, 0.65]
eig_complete_bf = [0.23, 0.01, 0.48, 0.93, 0.92, 0.5]

plt.bar(x, eig_complete_rs, width=width, label='RS', fc=color[0])
plt.bar(x + width, eig_complete_ga, width=width, label='GA', fc=color[1])
plt.bar(x + 2 * width, eig_complete_gs, width=width, label='GS', fc=color[2], tick_label=dataset)
plt.bar(x + 3 * width, eig_complete_msa, width=width, label='MSA', fc=color[3])
plt.bar(x + 4 * width, eig_complete_bf, width=width, label='BF', fc=color[4])
plt.xlabel("(b) Complete graph attack against EIG detection", fontsize=font_size)
plt.ylabel("$\mathcal{P}$", fontsize=font_size)

# Figure 3
ax3 = plt.subplot(2, 3, 3)
plt.ylim(0, 1)
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
# eig_ba_kara = [0.23, 0.39, 0.39, 0.39, 0.39]
# eig_ba_dol = [0.82, 0.86, 0.00, 0.91, 0.70]
# eig_ba_lesm = [0.29, 0.38, 0.38, 0.65, 0.47]
# eig_ba_polb = [0.90, 0.93, 0.88, 0.94, 0.93]
# eig_ba_footb = [0.71, 0.76, 0.83, 0.95, 0.80]
# eig_ba_faceb = [0.00, 0.68, 0.33, 0.50, 0.98]

eig_ba_rs = [0.23, 0.82, 0.29, 0.9, 0.71, 0.01]
eig_ba_ga = [0.39, 0.86, 0.38, 0.93, 0.76, 0.68]
eig_ba_gs = [0.39, 0.01, 0.38, 0.88, 0.83, 0.33]
eig_ba_msa = [0.39, 0.91, 0.65, 0.94, 0.95, 0.5]
eig_ba_bf = [0.39, 0.7, 0.47, 0.93, 0.8, 0.98]

plt.bar(x, eig_ba_rs, width=width, label='RS', fc=color[0])
plt.bar(x + width, eig_ba_ga, width=width, label='GA', fc=color[1])
plt.bar(x + 2 * width, eig_ba_gs, width=width, label='GS', fc=color[2], tick_label=dataset)
plt.bar(x + 3 * width, eig_ba_msa, width=width, label='MSA', fc=color[3])
plt.bar(x + 4 * width, eig_ba_bf, width=width, label='BF', fc=color[4])
plt.xlabel("(c) BA graph attack against EIG detection", fontsize=font_size)
plt.ylabel("$\mathcal{P}$", fontsize=font_size)

# Figure 4
ax4 = plt.subplot(2, 3, 4)
plt.ylim(0, 1)
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
# lab_tree_kara = [0.27, 0.26, 0.40, 0.80, 0.78]
# lab_tree_dol = [0.26, 0.48, 0.76, 0.80, 0.83]
# lab_tree_lesm = [0.12, 0.33, 0.46, 0.65, 0.85]
# lab_tree_polb = [0.50, 0.20, 0.70, 0.71, 0.90]
# lab_tree_footb = [0.12, 0.32, 0.24, 0.37, 0.26]
# lab_tree_faceb = [0.41, 0.25, 0.16, 0.50, 0.71]

lab_tree_rs = [0.27, 0.26, 0.12, 0.5, 0.12, 0.41]
lab_tree_ga = [0.26, 0.48, 0.33, 0.2, 0.32, 0.25]
lab_tree_gs = [0.4, 0.76, 0.46, 0.7, 0.24, 0.16]
lab_tree_msa = [0.8, 0.8, 0.65, 0.71, 0.37, 0.5]
lab_tree_bf = [0.78, 0.83, 0.85, 0.9, 0.26, 0.71]

plt.bar(x, lab_tree_rs, width=width, label='RS', fc=color[0])
plt.bar(x + width, lab_tree_ga, width=width, label='GA', fc=color[1])
plt.bar(x + 2 * width, lab_tree_gs, width=width, label='GS', fc=color[2], tick_label=dataset)
plt.bar(x + 3 * width, lab_tree_msa, width=width, label='MSA', fc=color[3])
plt.bar(x + 4 * width, lab_tree_bf, width=width, label='BF', fc=color[4])
plt.xlabel("(d) Tree graph attack against EIG detection", fontsize=font_size)
plt.ylabel("$\mathcal{P}$", fontsize=font_size)

# Figure 5
ax5 = plt.subplot(2, 3, 5)
plt.ylim(0, 1)
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
# lab_complete_kara = [0.24, 0.23, 0.24, 0.45, 0.24]
# lab_complete_dol = [0.70, 0.81, 0.46, 0.80, 0.91]
# lab_complete_lesm = [0.18, 0.19, 0.19, 0.37, 0.24]
# lab_complete_polb = [0.00, 0.19, 0.20, 0.19, 0.67]
# lab_complete_footb = [0.18, 0.00, 0.17, 0.60, 0.69]
# lab_complete_faceb = [0.00, 0.16, 0.37, 0.49, 0.00]

lab_complete_rs = [0.24, 0.7, 0.18, 0.01, 0.18, 0.01]
lab_complete_ga = [0.23, 0.81, 0.19, 0.19, 0.01, 0.16]
lab_complete_gs = [0.24, 0.46, 0.19, 0.2, 0.17, 0.37]
lab_complete_msa = [0.45, 0.8, 0.37, 0.19, 0.6, 0.49]
lab_complete_bf = [0.24, 0.91, 0.24, 0.67, 0.69, 0.01]

plt.bar(x, lab_complete_rs, width=width, label='RS', fc=color[0])
plt.bar(x + width, lab_complete_ga, width=width, label='GA', fc=color[1])
plt.bar(x + 2 * width, lab_complete_gs, width=width, label='GS', fc=color[2], tick_label=dataset)
plt.bar(x + 3 * width, lab_complete_msa, width=width, label='MSA', fc=color[3])
plt.bar(x + 4 * width, lab_complete_bf, width=width, label='BF', fc=color[4])
plt.xlabel("(e) Complete graph attack against LAB detection", fontsize=font_size)
plt.ylabel("$\mathcal{P}$", fontsize=font_size)

# Figure 6
ax6 = plt.subplot(2, 3, 6)
plt.ylim(0, 1)
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
# lab_ba_kara = [0.42, 0.43, 0.68, 0.82, 0.87]
# lab_ba_dol = [0.79, 0.89, 0.91, 0.91, 0.85]
# lab_ba_lesm = [0.18, 0.91, 0.20, 0.84, 0.92]
# lab_ba_polb = [0.89, 0.91, 0.91, 0.93, 0.92]
# lab_ba_footb = [0.44, 0.80, 0.73, 0.81, 0.85]
# lab_ba_faceb = [0.00, 0.98, 0.37, 0.56, 0.99]

# for i in range(5):
#     print([_[i] for _ in
#            [lab_ba_kara, lab_ba_dol, lab_ba_lesm,
#             lab_ba_polb, lab_ba_footb, lab_ba_faceb]])

lab_ba_rs = [0.42, 0.79, 0.18, 0.89, 0.44, 0.01]
lab_ba_ga = [0.43, 0.89, 0.91, 0.91, 0.8, 0.98]
lab_ba_gs = [0.68, 0.91, 0.2, 0.91, 0.73, 0.37]
lab_ba_msa = [0.82, 0.91, 0.84, 0.93, 0.81, 0.56]
lab_ba_bf = [0.87, 0.85, 0.92, 0.92, 0.85, 0.99]

plt.bar(x, lab_ba_rs, width=width, label='RS', fc=color[0])
plt.bar(x + width, lab_ba_ga, width=width, label='GA', fc=color[1])
plt.bar(x + 2 * width, lab_ba_gs, width=width, label='GS', fc=color[2], tick_label=dataset)
plt.bar(x + 3 * width, lab_ba_msa, width=width, label='MSA', fc=color[3])
plt.bar(x + 4 * width, lab_ba_bf, width=width, label='BF', fc=color[4])
# handles, labels = ax6.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', ncol=5)
plt.xlabel("(f) BA graph attack against LAB detection", fontsize=font_size)
plt.ylabel("$\mathcal{P}$", fontsize=font_size)

plt.show()
