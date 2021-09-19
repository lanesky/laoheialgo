# INPUT: 
# [
#   [1],
#   [0, 2],
#   [1, 3],
#   [1, 2]
# ]
def twoEdgeConnectedGraph(edges):
	if len(edges) == 0:
		return True
	seen = [-1] * len(edges)
	if getMinReachableDepth(0, -1, 0, seen, edges) == -1:
		return False
	return not (-1 in seen)

def getMinReachableDepth(curr, parent, currDepth, seen, edges):
	seen[curr] = currDepth
	minReachableDepth = currDepth
	
	for dest in edges[curr]:
		if seen[dest] == -1:
			minReachableDepth = min(minReachableDepth, getMinReachableDepth(dest, curr, currDepth + 1, seen, edges))
		elif dest != parent:
			minReachableDepth = min(minReachableDepth, seen[dest])
	
	if minReachableDepth == currDepth and parent != -1:
		return -1
	
	return minReachableDepth