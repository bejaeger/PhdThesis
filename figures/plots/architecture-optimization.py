
import numpy as np
import matplotlib.pyplot as plt

arch1 = [10.58, 10.605]
arch2 = [11.02, 10.47]
arch3 = [10.605, 10.38, 11.0, 11.06, 11.13, 11.35]
arch4 = [10.4, 10.55]
arch5 = [10.72, 10.8]

y = np.array([np.mean(a) for a in [arch1, arch2, arch3, arch4, arch5]])
print(y)
x = np.arange(1, 6, 1)


plt.plot(x, y, 'o', markersize=12, color="#0b80c3")

ax = plt.gca()
x_ticks_labels = ["A1", "A2", "A3", "A4", "A5"]
ax.set_xticks(x)
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=18)
ax.yaxis.grid(True, linestyle='-', color='gray')
#ax.xaxis.grid(True, linestyle='-', color='gray')
ax.set_xlim(0.5, 5.5)
ax.set_ylim(10.2, 11.2)

plt.xlabel('Architecture', fontsize=20)
plt.ylabel('Significance', fontsize=20)


#ax.tick_params(axis='both', which='major', labelsize=14)

plt.tight_layout()
#plt.show()
plt.savefig("arch-comparison.pdf")


