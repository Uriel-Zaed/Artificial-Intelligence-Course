import matplotlib.pyplot as plt

from static_func import *
from state import State
from a_star_man import A_Star_Man
from a_star_mis import A_Star_Mis


N = 3 # Must be odd
num_of_problems = 3

initial_states = initial_states(num_of_problems,N)

w_s = [1,1.5,2,4,5]
# w_s = [1,1.5,2,2.5,3,3.5,4]

moves_man = {w:0 for w in w_s} # dict key=w, value=moves
moves_mis = {w:0 for w in w_s} # dict key=w, value=moves
logical_steps_man = {w:0 for w in w_s} # dict key=w, value=steps
logical_steps_mis = {w:0 for w in w_s} # dict key=w, value=steps
sol_man = {} # dict key=w, value=sol
sol_mis = {} # dict key=w, value=sol

for i_s in initial_states:
    for w in w_s:
        a_star_man = A_Star_Man(i_s,goal_state(N),N,w)
        a_star_man.solve()
        moves_man[w] += a_star_man.num_of_moves/num_of_problems
        logical_steps_man[w] += a_star_man.logical_steps/num_of_problems
        sol_man[w] = a_star_man.solution

        a_star_mis = A_Star_Mis(i_s,goal_state(N),N,w)
        a_star_mis.solve()
        moves_mis[w] += a_star_mis.num_of_moves/num_of_problems
        logical_steps_mis[w] += a_star_mis.logical_steps/num_of_problems
        sol_mis[w] = a_star_mis.solution

    
plt.plot(w_s, logical_steps_man.values(), 'o-', label='Manhetten')
plt.plot(w_s, logical_steps_mis.values(), 'o-', label='Missplaced')
plt.legend()
plt.xlabel("weight")
plt.ylabel("logical steps")
plt.title(f"Weighted A*")
plt.show()

plt.plot(w_s, logical_steps_man.values(), 'o-', label='Manhetten')
plt.legend()
plt.xlabel("weight")
plt.ylabel("logical steps")
plt.title(f"Weighted A*")
plt.show()


plt.plot(w_s, moves_man.values(), 'o-', label='Manhetten')
plt.plot(w_s, moves_mis.values(), 'o-', label='Missplaced')
plt.legend()
plt.xlabel("weight")
plt.ylabel("number of moves")
plt.title(f"Weighted A*")
plt.show()