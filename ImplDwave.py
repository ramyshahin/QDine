import DiningPhilosophers as dp
import matplotlib.pyplot as plt
import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import time 

def atMost1(a,b):
    return not (a and b)

def exactly1(a,b):
    return (a or b) and atMost1(a,b)

class ImplDwave(dp.DiningPhilosophers):
    def __init__(self, N, draw=True):
        dp.DiningPhilosophers.__init__(self, N, draw)

    def getSampler(self):
        return EmbeddingComposite(DWaveSampler())

    def solve(self, checkDeadloack=True):
        csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
        for i in range(self.N):
            c = self.chopsticks[i]
            next_c = self.chopsticks[(i+1) % self.N]
            vars = [c + '_R', c + '_L'] 
            if checkDeadloack:
                csp.add_constraint(exactly1, vars)
            else: csp.add_constraint(atMost1, vars)

            phils = [c + '_R', next_c + '_L']
            if checkDeadloack:
                csp.add_constraint(exactly1, phils)

        bqm = dwavebinarycsp.stitch(csp)

        sampler = self.getSampler()
        try:
            start = time.time()
            response = sampler.sample(bqm, num_reads=50)
            end = time.time()
            t = end - start
            sample = next(response.samples())
            if not csp.check(sample):
                print("Failed to detect deadlock")
                t = 0
            else:
                if self.draw: self.drawConfig(sample)
        except:
            t = -1

        return t
