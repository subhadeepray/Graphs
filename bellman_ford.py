from numpy import matrix
from numpy import array

adjacencylist = matrix([[0.0, -1.0,4.0 ,float('inf') ,float('inf')],
						[float('inf'), 0.0 ,3.0, 2.0 ,2.0],
						[float('inf'), float('inf') ,0.0 ,float('inf') ,float('inf')],
						[float('inf'), 1.0 ,5.0 ,0.0 ,float('inf')],
						[float('inf'),float('inf') ,float('inf'),-3.0 ,0.0]])

print adjacencylist

def bellmanFord(G,s):
	d = []
	for vertex in range(len(G)):
			d.append(float('inf'))
	d[s] = 0
	for vertex in range(len(G)-1):
		for u in range(len(array(G).tolist())):
			for v in range(len(array(G).tolist()[u])):
				d[v] = min(d[v],d[u]+array(G).tolist()[u][v])

	for u in range(len(array(G).tolist())):
		for v in range(len(array(G).tolist()[u])):
			if d[v] > d[u] + array(G).tolist()[u][v]:
				return "Negative Cycle Encountered"
	return d

print bellmanFord(adjacencylist,0)