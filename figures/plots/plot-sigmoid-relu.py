import numpy as np
import matplotlib.pyplot as plt
 
# Sigmoid function
#
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Creating sample Z points
#
z = np.arange(-6, 6, 0.1)
 
# Invoking Sigmoid function on all Z points
#
phi_z = sigmoid(z)

# Plotting the Sigmoid function
#
plt.plot(z, phi_z, linewidth=3, color="#0b80c3", label=r"$\sigma(x) = \frac{1}{1 + e^{-x}}$")
plt.legend(fontsize=25, loc='upper left', frameon=False, handlelength=1.5)
plt.axvline(0.0, color='grey', linestyle='--')
plt.xlabel('x', fontsize=20)
#plt.ylabel('$\sigma(x)$', fontsize=20)
plt.yticks([0, 0.5, 1])
ax = plt.gca()
ax.yaxis.grid(True, linestyle='--')
ax.tick_params(axis='both', which='major', labelsize=14)

plt.tight_layout()
#plt.show()
plt.savefig("sigmoid.pdf")
plt.close()


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
plt.plot(z, phi_z, linewidth=3, color="#0b80c3", label=r"$R(x) = \max(0,x)$")
plt.legend(fontsize=25, loc='upper left', frameon=False,handlelength=1.5)
plt.axvline(0.0, color='grey', linestyle='--')
plt.xlabel('x', fontsize=20)
#plt.ylabel('$R(x)$', fontsize=20)

plt.yticks([-0.1, 0, 1])
plt.xticks(np.arange(min(z), max(z)+1, 2))
plt.yticks([0, 1])
#plt.yticks([np.arange(min(phi_z), max(phi_z)+1, 4)])

ax = plt.gca()
ax.yaxis.grid(True, linestyle='--')
ax.tick_params(axis='both', which='major', labelsize=14)
plt.tight_layout()
#plt.show()
plt.savefig("relu.pdf")

