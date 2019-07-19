# modified version of https://github.com/rigetti/grove/blob/master/examples/GroversAlgorithm.ipynb

from itertools import product

from mock import patch

from grove.amplification.grover import Grover

from pyquil.api import QVMConnection

import matplotlib.pyplot as plt

import numpy as np
from collections import Counter

N = 4
target_bitstring0 = ''
target_bitstring1 = ''
for i in range(N):
    if (i % 2):
        target_bitstring0 += '01'
        target_bitstring1 += '10'
    else:
        target_bitstring0 += '10'
        target_bitstring1 += '01'
    
print(target_bitstring0)
print(target_bitstring1)

bit = ("0", "1")
bitstring_map = {}
target_bitstring_phase = -1
nontarget_bitstring_phase = 1

# We construct the bitmap for the oracle
for bitstring in product(bit, repeat=N*2):
    bitstring = "".join(bitstring)
    if bitstring == target_bitstring0 or bitstring == target_bitstring1:
        bitstring_map[bitstring] = target_bitstring_phase
    else:
        bitstring_map[bitstring] = nontarget_bitstring_phase

qvm = QVMConnection()
#with patch("pyquil.api.QuantumComputer") as qc:
#qvm.run.return_value = [[int(bit) for bit in target_bitstring]]

grover = Grover()
samples = []
for i in range(50):
    found_bitstring = grover.find_bitstring(qvm, bitstring_map)
    samples.append(found_bitstring)

c = Counter(samples)
print(c)
plt.bar(*zip(*c.most_common()), width=.5, color='g')
plt.show()