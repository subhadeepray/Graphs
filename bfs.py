from numpy import matrix
from numpy import array

adjacencylist = matrix([[0, 1 ,1 ,1 ,0],
						[1, 0 ,0 ,0 ,0],
						[1, 0 ,0 ,0 ,1],
						[1, 0 ,0 ,0 ,0],
						[0, 0 ,1 ,0 ,0]])

print adjacencylist

def BFS(G,s):
	color,d,pi = [],[],[] #color of the node visited, distance from s, pi tracks the predecessor of a node
	for vertex in range(len(G)):
		color.append("white")
		d.append(float('inf'))
		pi.append(None)
	queue = []
	color[s] = "grey"
	d[s] = 0
	pi[s] = None
	queue.append(s)
	while len(queue) > 0:
		u = queue.pop(0)
		adj = [i for i in range(len(array(G)[u].tolist())) if array(G)[u].tolist()[i] == 1]
		for v in adj:
			if color[v] == "white":
				color[v] = "grey"
				d[v] = d[u] + 1
				pi[v] = u
				queue.append(v)
			color[u] = "black"
	print color,d,pi
	print d[0]
	prev = d[1]
	l = []
	for i in range(1,len(d)):
		if prev == d[i]:
			l.append(i)
		else:
			print l
			print i
		prev = d[i]



BFS(adjacencylist,0)