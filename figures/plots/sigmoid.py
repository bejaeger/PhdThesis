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
plt.plot(z, phi_z, linewidth=3, color="#0b80c3")
plt.axvline(0.0, color='grey', linestyle=':')
plt.xlabel('x')
plt.ylabel('$\sigma(x)$')
plt.yticks([0, 0.5, 1])
ax = plt.gca()
ax.yaxis.grid(True)
plt.tight_layout()
#plt.show()
plt.savefig("sigmoid.pdf")