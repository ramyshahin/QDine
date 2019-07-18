# demonstrating the dining philosopher's problem
# not actually searching for a deadlock state here
import ImplDwave as dp
import matplotlib.pyplot as plt

p = dp.ImplDwave(7)
p.solve(False)
