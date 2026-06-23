import matplotlib.pyplot as plt
import numpy as np

params = {
    "legend.fontsize": "large",
    "axes.labelsize": "x-large",
    "axes.titlesize": "x-large",
    "xtick.labelsize": "x-large",
    "ytick.labelsize": "x-large",
    "xtick.direction": "in",
    "ytick.direction": "in",
}
plt.rcParams.update(params)
dat = np.loadtxt(
    "/storage/brno12-cerit/home/poledto1/HydroIsing-2DTExS/EoSmub500/invIsing-2DTExSmub500.dat"
)

NTt, Nmbt = 500, 500
dat = dat.reshape(NTt, Nmbt, -1)

fig, ax = plt.subplots(1, 1, figsize=(9, 8))
for i in range(Nmbt):
    arr = dat[:, i]
    T, e = arr[:, 4], arr[:, 2]
    ax.plot(T, e / T**4, lw=1)
ax.set_xlabel("$T$ (GeV)")
ax.set_ylabel("$\\epsilon/T^4$")
plt.savefig("Teps.png", format="png", dpi=300)
plt.show()


fig, ax = plt.subplots(1, 1, figsize=(9, 8))
for i in range(NTt - 340):  # To see the 1st order line under the folding.
    arr = dat[i, :]
    mub, nb, T = arr[:, 5], arr[:, 3], arr[:, 4]
    ax.plot(nb / T**3, mub, lw=1)

ax.set_xlabel("$n_B/T^3$")
ax.set_ylabel("$\\mu_B$ (GeV)")
ax.set_xlim(-0.05, 1.64)
plt.savefig("mubnb.png", format="png", dpi=300)
plt.show()


fig, ax = plt.subplots(1, 1, figsize=(9, 8))
for i in range(NTt - 340):  # To see the 1st order line under the folding.
    arr = dat[i, :]
    chi2, nb, T = arr[:, 9], arr[:, 3], arr[:, 4]
    ax.plot(nb / T**3, chi2 / T**2, lw=1)

ax.set_xlabel("$n_B/T^3$")
ax.set_ylabel("$\\chi_2/T^2$")
ax.set_xlim(-0.05, 1.37)
# ax.set_xlim(0.41, 0.66)
ax.set_ylim(-0.01, 0.9)
plt.savefig("chinb.png", format="png", dpi=300)
plt.show()
