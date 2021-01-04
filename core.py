import random
import numpy as np
import time

beginning = time.perf_counter()


P_YELLOW = 0.48
P_GREEN = 0.24
P_BLUE = 0.16
P_PURPLE = 0.08
P_RED = 0.04

options = ["y", "g", "b", "p", "r"]

num_spins = 2000
successes = 0



scrap_allocation = np.array([0.67, 0.33, 0, 0 ,0])

best_rate = 0
best_allocation = None

for y in np.arange(0, 1, 0.05):
    for g in np.arange(0, 1-y, 0.05):
        for b in np.arange(0, 1-(y+g), 0.05):
            for p in np.arange(0, 1-(y+g+b), 0.05):
                r = 1-(y+g+b+p)
                scrap_allocation = np.array([y, g, b, p, r])
                successes = 0
                for spin in range(num_spins):
                    num_betted = 100
                    bet = num_betted * scrap_allocation

                    revenue = 0
                    selection = np.random.choice(options, size=1, p=np.array([P_YELLOW, P_GREEN, P_BLUE, P_PURPLE, P_RED]))[0]
                    if selection == "y":
                        revenue += (bet[0] * 2)
                    elif selection == "g":
                        revenue += (bet[1] * 4)
                    elif selection == "b":
                        revenue += (bet[2] * 6)
                    elif selection == "p":
                        revenue += (bet[3] * 12)
                    elif selection == "r":
                        revenue += (bet[4] * 25)
                    if revenue > num_betted:
                        successes += 1
                success_rate = successes / num_spins
                if success_rate > best_rate:
                    best_allocation = scrap_allocation
                    best_rate = success_rate
end = time.perf_counter()

print (end-beginning)
print (best_allocation)
print (best_rate)

