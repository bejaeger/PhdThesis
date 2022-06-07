
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches


####################
# Configuration

# EW scan plot
ewscanplot = True

# these are the columns
# ,Z0_opt_bins_val,Z0_opt_bins_train,Z0_opt_bins_test,Z0unc_opt_bins_val,Z0unc_opt_bins_train,Z0unc_opt_bins_test,Z0_40bins_val,Z0_40bins_train,Z0_40bins_test,rel_ewww_highest_bin_val,rel_ewww_highest_bin_train,rel_ewww_highest_bin_test,learning_rate,weight_EWWW
data = np.genfromtxt("all_metrics_no_bins.csv", skip_header=2, delimiter=",")

# indizes
ilr = 13
iew_weight = 14
iew_contr = 10
iZ0 = 1
iZ0unc = 4
iZ040bin = 7

Z0 = np.array([x[iZ0] for x in data])
Z0unc = np.array([x[iZ0unc] for x in data])
Z040bin = np.array([x[iZ040bin] for x in data])
lr = np.array([x[ilr] for x in data])
ew_weight = np.array([x[iew_weight] for x in data])
ew_contr = np.array([x[iew_contr] for x in data])


Z0max = [max(Z0[np.where(lr == it_lr)]) for it_lr in np.unique(lr)]
lrunique = np.unique(lr)
ew_weight_unique = np.unique(ew_weight)

chosen_eww = 0.08
Z0_ew08 = [Z0[np.where( (lr == it_lr)  & (ew_weight == chosen_eww) )] for it_lr in np.unique(lr)]
Z0unc_ew08 = [Z0unc[np.where( (lr == it_lr)  & (ew_weight == chosen_eww) )] for it_lr in np.unique(lr)]
Z040bin_ew08 = [Z040bin[np.where( (lr == it_lr)  & (ew_weight == chosen_eww) )] for it_lr in np.unique(lr)]


chosen_lr = 9
Z0_lr9 = [Z0[np.where( (lr == chosen_lr)  & (ew_weight == it_ew) )] for it_ew in np.unique(ew_weight)]
Z0unc_lr9 = [Z0unc[np.where( (lr == chosen_lr)  & (ew_weight == it_ew) )] for it_ew in np.unique(ew_weight)]
Z040bin_lr9 = [Z040bin[np.where( (lr == chosen_lr)  & (ew_weight == it_ew) )] for it_ew in np.unique(ew_weight)]
ew_contr = [ew_contr[np.where( (lr == chosen_lr)  & (ew_weight == it_ew) )] for it_ew in np.unique(ew_weight)]

markersize = 10


##########################
# Configuration

# ew scan
x = ew_weight_unique
y1 = Z040bin_lr9
y2 = Z0_lr9
y3 = Z0unc_lr9
y4 = ew_contr
xtitle = 'EW $WW$ training weight fraction'
filename = "sig_vs_ew_fraction_lr9.pdf"

# ew scan
if not ewscanplot:
    x = lrunique
    y1 = Z040bin_ew08 
    y2 = Z0_ew08 
    y3 = Z0unc_ew08
    xtitle = 'Learning rate'
    filename = "sig_vs_lrate.pdf"


fig, ax = plt.subplots()
sig_color='#F17105' if ewscanplot is True else "black"
frac_color="#0b80c3"
if ewscanplot:
    plt.plot(x,y1, '^', color=sig_color, markersize=markersize, label="Z0 w/ 40 bins")
    plt.plot(x, y2, 'o', color=sig_color, markersize=markersize, label="Z0 w/ var. bins")
    plt.plot(x, y3, 'v', color=sig_color, markersize=markersize, label="Z0+unc. w/ var. bins")
else:
    plt.plot(x, y2, 'o', color=sig_color, markersize=markersize)



ax.yaxis.grid(True, linestyle='-', color='gray')
if ewscanplot:
    plt.ylim((5.4, 12.6))
    ax.tick_params(axis='y', colors=sig_color)
    ax.yaxis.label.set_color(sig_color)
    ax.set_ylabel(r'Significance', fontsize=14, color=sig_color)
else:
    ax.set_ylabel('Significance', fontsize=14)
    plt.ylim((7, 11))
plt.legend(frameon=True, fancybox=True, loc='upper left', numpoints=1)
ax.set_xlabel(xtitle, fontsize=14)

plt.xlim((2, 22))

#if not ewscanplot:
#    e1 = patches.Ellipse((9, 9.83), 1.1, 0.5,
#                         linewidth=2, fill=False, zorder=2, color='red')
#    ax.add_patch(e1)

if ewscanplot:
    #plt.text(0.045, 5.68, "Learning rate = 9", fontsize=14)

    ax2 = plt.twinx()

    ax2.spines['right'].set_color(frac_color)
    ax2.tick_params(axis='y', colors=frac_color)
    ax2.yaxis.label.set_color(frac_color)
    ax2.title.set_color(frac_color)
    plt.plot(x, y4, 's', color=frac_color, markersize=markersize, label = "EW $WW$ fraction")
    
    e1 = patches.Ellipse((0.12, 0.225), 0.02, 0.13,
                         linewidth=2, fill=False, zorder=2, color='black')
    ax2.add_patch(e1)


    plt.legend(frameon=True, fancybox=True, loc='upper right', numpoints=1)

    fontsize = 14
    ax2.set_ylabel('EW $WW$ fraction of total Bkg.', fontsize=14)
    plt.ylim((0.14, 0.35))
    plt.xlim((0.04, 0.21))
    
#plt.text(min(x)+(max(x)-min(x))*0.05, min(y)+(max(y)-min(y))*0.05, "lrate = 9", )
ax.tick_params(axis='y', which='major', labelsize=12)


    
plt.tight_layout()
#plt.show() 
plt.savefig(filename)
plt.savefig(filename)


