import random
import numpy as np


P_YELLOW = 0.48
P_GREEN = 0.24
P_BLUE = 0.16
P_PURPLE = 0.08
P_RED = 0.04

num_scraps = 1000
num_betted = 500

options = ["y", "g", "b", "p", "r"]

scrap_allocation = np.array([0.67, 0.33, 0, 0 ,0])

bet = num_scraps * scrap_allocation

print (bet)

num_spins = 10

for spin in range(num_spins):
    num_betted = num_scraps // 2
    bet = num_betted * scrap_allocation
    num_scraps = num_scraps - num_betted

    selection = np.random.choice(options, size=1, p=np.array([P_YELLOW, P_GREEN, P_BLUE, P_PURPLE, P_RED]))[0]
    if selection == "y":
        num_scraps += bet[0]
    elif selection == "g":
        num_scraps += bet[1]
    elif selection == "b":
        num_scraps += bet[2]
    elif selection == "p":
        num_scraps += bet[3]
    elif selection == "r":
        num_scraps += bet[4]
    print (num_scraps)

