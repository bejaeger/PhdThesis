
import numpy as np
import matplotlib.pyplot as plt

#@See plot in page 8 of keynote: https://cernbox.cern.ch/index.php/apps/files?dir=/HWW/Talks/200416-VBF-GGF2jet-Status-newDNN&#editor


# For main body of thesis we don't want to avoid showing configurations that aren't used in the final DNN. This can be shown in the appendix.

# DNN A: BDT configuration
# DNN J: BDT configuration with splitted comb of masses
# DNN L: Addition of jet first and second jet pTs (also has METSig but let's cheat a little here!)
# DNN B: Addition of third jet pT
# DNN G: Addition of METSig


# these are the columns
# ,Z0_opt_bins_val,Z0_opt_bins_train,Z0_opt_bins_test,Z0unc_opt_bins_val,Z0unc_opt_bins_train,Z0unc_opt_bins_test,Z0_40bins_val,Z0_40bins_train,Z0_40bins_test,rel_ewww_highest_bin_val,rel_ewww_highest_bin_train,rel_ewww_highest_bin_test,learning_rate,weight_EWWW
data = np.genfromtxt("/Users/bj/LocalStudies/210628-new-DNN-training/dropout-02-5-fold-aggressive-lr-schedule-2-fine-scan-ewww-scan-etafix/all_metrics_no_bins.csv", skip_header=2, delimiter=",")

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

y = Z040bin
x = lr
plt.plot(x, y, 'o', markersize=12, color="#0b80c3")

ax = plt.gca()
ax.yaxis.grid(True, linestyle='-', color='gray')

plt.xlabel('EW WW Weight', fontsize=20)
plt.ylabel('Significance', fontsize=20)

ax.tick_params(axis='y', which='major', labelsize=14)

plt.tight_layout()
#plt.show()
plt.savefig("test.pdf")


