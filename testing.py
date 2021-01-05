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

num_spins = 50000
successes = 0



scrap_allocation = np.array([0.55, 0.3, 0, 0.1,0.05])

best_rate = 0
best_allocation = None

revenues = []

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
    revenues.append(revenue)
success_rate = successes / num_spins
average_revenue = np.mean(np.array(revenues))
std_revenue = np.std(np.array(revenues))
print ("Profit rate: " + str(round(success_rate, 3)))
print ("Average revenue: " + str(round(average_revenue, 3)))
print ("Std revenue: " + str(round(std_revenue, 3)))
print ("Ratio revenue to input: " + str(round(average_revenue/num_betted, 3)))


