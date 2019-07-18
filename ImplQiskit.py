import DiningPhilosophers as dp
from qiskit import Aer, IBMQ
from qiskit.aqua.components.oracles import logical_expression_oracle
from qiskit.aqua.algorithms import Grover
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt

def exactly1(a,b):
    return '(' + a + ' ^ ' + b + ')'

class ImplQiskit(dp.DiningPhilosophers):
    def __init__(self, N, draw=True):
        dp.DiningPhilosophers.__init__(self, N, draw)

    def solve(self): 
        constraints = ""
        index = []
        for i in range(self.N):
            c = self.chopsticks[i]
            next_c = self.chopsticks[(i+1) % self.N]
            if (i > 0): constraints += ' & '
            constraints += exactly1(c + '_R', c + '_L')
            constraints += ' & '
            constraints += exactly1(c + '_R', next_c + '_L')

            if i % 2 == 0:
                index.append(c + '_R')
                index.append(c + '_L')
            else:
                index.append(c + '_L')
                index.append(c + '_R')

        backend = Aer.get_backend('qasm_simulator')
        #IBMQ.load_account()
        #backend = IBMQ.get_backend('ibmq_16_melbourne')
        print(backend.configuration())
        
        oracle = logical_expression_oracle.LogicalExpressionOracle(
                    constraints) #, mct_mode='advanced', optimization='espresso')
        algorithm = Grover(oracle)
        result = algorithm.run(backend)

        hist = plot_histogram(result["measurement"], title='measurement distribution')
        hist.show()
        hist.savefig('qiskit.png')
        print(index)
        print(result["result"])
        for r in (result["result"]):
            i = abs(r) - 1
            if r < 0: print('~' + index[i])
            else: print(index[i])

s = ImplQiskit(2)
s.solve()