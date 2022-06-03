import numpy as np
import matplotlib.pyplot as plt
 
def ReLU(x):
    return x * (x > 0)

# Creating sample Z points
#
z = np.arange(-2, 2, 0.1)
 
# Invoking Sigmoid function on all Z points
#
phi_z = ReLU(z)

# Plotting the Sigmoid function
#
plt.plot(z, phi_z, linewidth=3, color="#0b80c3")
plt.axvline(0.0, color='grey', linestyle=':')
plt.xlabel('x', fontsize=20)
plt.ylabel('$R(x)$', fontsize=20)

plt.yticks([-0.1, 0, 2])
plt.xticks(np.arange(min(z), max(z)+1, 2))
plt.yticks([0, 2])
#plt.yticks([np.arange(min(phi_z), max(phi_z)+1, 4)])

ax = plt.gca()
ax.yaxis.grid(True)
plt.tight_layout()
#plt.show()
plt.savefig("relu.pdf")

