import matplotlib.pyplot as plt
import numpy as np

from static_func import *
from a_star_man import A_Star_Man
from a_star_mis import A_Star_Mis


N = 3 # Must be odd
num_of_problems = 10

initial_states = generate_initial_states(num_of_problems,N)

w_p = 2 # print solotion

w_s = [1,2] 
# w_s = [1,1.5,2,2.5,3,3.5,4]

moves_man = {w:0 for w in w_s} # dict key=w, value=moves
moves_mis = {w:0 for w in w_s} # dict key=w, value=moves
logical_steps_man = {w:0 for w in w_s} # dict key=w, value=steps
logical_steps_mis = {w:0 for w in w_s} # dict key=w, value=steps
sol_man = {} # dict key=w, value=sol
sol_mis = {} # dict key=w, value=sol

for i_s in initial_states:
    for w in w_s:
        a_star_man = A_Star_Man(i_s,generate_goal_state(N),N,w)
        a_star_man.solve()
        moves_man[w] += a_star_man.num_of_moves/num_of_problems
        logical_steps_man[w] += a_star_man.logical_steps/num_of_problems
        sol_man[w] = a_star_man.solution

        a_star_mis = A_Star_Mis(i_s,generate_goal_state(N),N,w)
        a_star_mis.solve()
        moves_mis[w] += a_star_mis.num_of_moves/num_of_problems
        logical_steps_mis[w] += a_star_mis.logical_steps/num_of_problems
        sol_mis[w] = a_star_mis.solution

############### Prints ##################
print("A* solution example with manhattan hueristic:")
for i, s in enumerate(sol_man[1]):
    if i == 0:
        print("initial state:")
    elif i == len(sol_man[1])-1:
        print(f"move {i} (goal state):")
    else:
        print(f"move {i}:")
    s.print()

print(f"Weighted A* (w={w_p}) solution example with manhattan hueristic:")
for i, s in enumerate(sol_man[w_p]):
    if i == 0:
        print("initial state:")
    elif i == len(sol_man[w_p])-1:
        print(f"move {i} (goal state):")
    else:
        print(f"move {i}:")
    s.print()

############### Plots ###################
x = np.arange(len(w_s))  # the label locations

width = 0.35  # the width of the bars

fig, ax = plt.subplots()

# Plotting the bars
bars1 = ax.bar(x - width/2, logical_steps_man.values(), width, label='manhattan')
bars2 = ax.bar(x + width/2, logical_steps_mis.values(), width, label='missplaced-r-c')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{:.2f}'.format(height).format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Adding labels, title, and custom x-axis tick labels
ax.set_xlabel('weight', fontsize=16)
ax.set_ylabel('logical steps', fontsize=16)
ax.set_title('Logical steps - Weighted A*', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(w_s)
ax.legend()

# Displaying the plot
plt.show()

x = np.arange(len(w_s))  # the label locations

width = 0.35  # the width of the bars

fig, ax = plt.subplots()

# Plotting the bars
bars1 = ax.bar(x - width/2, moves_man.values(), width, label='manhattan')
bars2 = ax.bar(x + width/2, moves_mis.values(), width, label='mis')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{:.2f}'.format(height).format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Adding labels, title, and custom x-axis tick labels
ax.set_xlabel('weight', fontsize=16)
ax.set_ylabel('moves', fontsize=16)
ax.set_title('Moves - Weighted A*', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(w_s)
ax.legend()

# Displaying the plot
plt.show()

