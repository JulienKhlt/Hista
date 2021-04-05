from math import sqrt
import numpy as np
from random import randint, random, normalvariate
import matplotlib.pyplot as plt

delta = 0.64
sigma = sqrt(0.2)
alpha = 0


def eta(u, t):
    return np.sign(u) * np.maximum(np.abs(u) - t, 0)


def r():
    if randint(0, 1) == 1:
        return 1
    else:
        return -1


def B(p):
    if random() > p:
        return 1
    else:
        return 0


def resoudre_equation(a):
    pass


def compute_esperance(nb, p):
    for i in range(nb):
        theta = r() * B(p)
        Z = normalvariate(0, 1)
        resoudre_equation(alpha)


def plot_eta(t_values=None):
    if t_values is None:
        t_values = [1, 2, 3]
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, figsize=(14, 6))
    mu = np.linspace(-5, 5, 50)

    ax0.set_title(r"$\eta(\mu,t)$ with $t=1$")
    ax0.plot(mu, eta(mu, t_values[0]))

    ax1.set_title(r"$\eta(\mu,t)$ with $t=2$")
    ax1.plot(mu, eta(mu, t_values[1]))

    ax2.set_title(r"$\eta(\mu,t)$ with $t=3$")
    ax2.plot(mu, eta(mu, t_values[2]))

    fig.suptitle(r"Plotting of $\eta(\mu, t)$ for $t=1,2,3$")
    plt.show()
    return
