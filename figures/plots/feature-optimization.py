
import numpy as np
import matplotlib.pyplot as plt

#@See plot in page 8 of keynote: https://cernbox.cern.ch/index.php/apps/files?dir=/HWW/Talks/200416-VBF-GGF2jet-Status-newDNN&#editor


# For main body of thesis we don't want to avoid showing configurations that aren't used in the final DNN. This can be shown in the appendix.

# DNN A: BDT configuration
# DNN J: BDT configuration with splitted comb of masses
# DNN L: Addition of jet first and second jet pTs (also has METSig but let's cheat a little here!)
# DNN B: Addition of third jet pT
# DNN G: Addition of METSig


sign = [7.7, 8.57, 9.55, 10.92, 11.5]

y = sign
x = np.arange(1, len(sign)+1, 1)


plt.plot(x, y, 'o', markersize=12, color="#0b80c3")

ax = plt.gca()
x_ticks_labels = ["S1", "S2", "S3", "S4", "S5"]
ax.set_xticks(x)
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=18)
ax.yaxis.grid(True, linestyle='-', color='gray')
#ax.xaxis.grid(True, linestyle='-', color='gray')
ax.set_xlim(0.5, len(sign)+0.5)
ax.set_ylim(7, 12)


text = (r"S1: Baseline"
        "\n"
        "S2: Baseline w/  split $m_{l*j*}$"
        "\n"
        "S3: S2 + $\it{p}_{\mathrm{T}}^{j0}$, $\it{p}_{\mathrm{T}}^{j1}$"
        "\n"
        "S4: S3 + $\it{p}_{\mathrm{T}}^{j2}$"
        "\n"
        "S5: S4 + $E_{\mathrm{T}}^{\mathrm{miss}} \mathrm{Sign.}$"
)
ax.text(0.8, 10.1, text, fontsize=16, bbox=dict(facecolor='white', pad=20))

plt.xlabel('Set of Variables', fontsize=20)
plt.ylabel('Significance', fontsize=20)


ax.tick_params(axis='y', which='major', labelsize=14)

plt.tight_layout()
#plt.show()
plt.savefig("feature-comparison.pdf")


