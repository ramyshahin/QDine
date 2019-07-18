import networkx as nx
import matplotlib.pyplot as plt

class DiningPhilosophers:
    def __init__(self, N, draw=True):
        self.N = N
        self.draw = draw
        self.philosophers = ['phil' + str(i) for i in range(N)]
        self.chopsticks = ['stick' + str(i) for i in range(N)]

    def drawConfig(self, config):  
        G = nx.Graph()
        alternating=[]
        sizes=[]
        colors=[]
        shapes=[]
        for i in range(self.N):
            alternating.append(self.philosophers[i])
            sizes.append(30000/self.N) 
            colors.append('skyblue')
            shapes.append('o')
            alternating.append(self.chopsticks[i])
            sizes.append(5000/self.N)
            colors.append('y')
            shapes.append('o')

        G.add_nodes_from(alternating)
        for i in range(self.N):
            c = self.chopsticks[i]
            if (config[c + '_L']):
                G.add_edge(c, self.philosophers[i])
            if (config[c + '_R']):
                G.add_edge(c, self.philosophers[(i+1) % self.N])

        nx.draw_circular(G, with_labels=True, node_size=sizes, node_color=colors, node_shape='o')
        plt.show() 


