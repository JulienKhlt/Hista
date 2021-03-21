from math import sqrt
import numpy as np
from random import randint, random, normal

δ = 0.64
σ = sqrt(0.2)

def η(u, t):
    return np.sign(u) * max(abs(u) - t, 0)

def r():
    if (randint(0, 1) == 1):
        return 1
    else :
        return -1

def B(p):
    if (random() > p):
        return 1
    else :
        return 0


def compute_esperance(nb, p):
    for i in range(nb):
        θ = r() * B(p)
        Z = normal()
        resoudre_equation(α, )
        
