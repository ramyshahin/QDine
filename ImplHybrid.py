import ImplDwave as dp
from hybrid.reference.kerberos import KerberosSampler
from dwave.system.composites import AutoEmbeddingComposite
import matplotlib.pyplot as plt

class ImplHybrid(dp.ImplDwave):
    def getSampler(self):
        return AutoEmbeddingComposite(KerberosSampler())

Ns = []
times = []
for i in range(20,1001,20):
    Ns.append(i)
    p = ImplHybrid(i, draw=False)
    t = p.solve()
    times.append(t)

plt.xlabel('N')
plt.ylabel('t(s)')
plt.plot(Ns, times, 'bo')
plt.show()