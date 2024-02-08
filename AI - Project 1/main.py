
from problem import Problem
from branch_and_bound import BranchAndBound
import matplotlib.pyplot as plt

N = 5
D = 5
num_of_problems = 10
p1 = [0.4, 0.7]
p2 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
problems = []

graphs = {}

for p_1 in p1:
    graph_p2 = []
    graph_cc = []

    for p_2 in p2:
        average_CC = 0
        for _ in range(num_of_problems):
            pr = Problem(N,D,p_1,p_2)
            bnb = BranchAndBound(pr)
            bnb.solver()
            average_CC += pr.CC/num_of_problems
        graph_p2.append(p_2)
        graph_cc.append(average_CC)
    graphs[p_1] = (graph_p2, graph_cc)
        
for p_1 in graphs:
    plt.plot(graphs[p_1][0], graphs[p_1][1])
    plt.title(f"B&B p1 = {p_1}")
    plt.show()
