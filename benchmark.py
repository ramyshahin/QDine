import ImplDwave as dp
import matplotlib.pyplot as plt
import time

Ns = []
times = []
for i in range(5,301,5):
    Ns.append(i)
    p = dp.ImplDwave(i, draw=False)
    t = p.solve()
    times.append(t)

plt.xlabel('N')
plt.ylabel('t(s)')
plt.plot(Ns, times, 'bo')
plt.show()