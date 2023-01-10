# -*- coding: utf-8 -*-
"""
@author: t.maybour
"""

import numpy as np

#################################################################################
#################################################################################

def main():

    #############################
    
    source = 0
    target = 10
    
    faults = []    

    conns = [
        [0,1,1],
        [0,2,2],
        [0,3,3],
        [1,4,2],
        [2,4,3],
        [2,5,1],
        [2,6,4],
        [3,5,2],
        [4,8,3],
        [5,7,4],
        [5,9,5],
        [6,8,4],        
        [7,10,2],
        [8,10,1],
        [9,10,1]
    ]

    working_conns = []
    for x in conns:
        if len(set(x).intersection(set(faults))) == 0:
            working_conns.append(x)

    node_ids = list(set([x[0] for x in working_conns]+[x[1] for x in working_conns]))

    graphs = []
    graph_pos = {}
    for node_id in node_ids:
        graphs.append(node(node_id))
        graph_pos[node_id] = len(graphs)-1

    for conn in working_conns:
        graphs[graph_pos[conn[0]]].outputs.append(conn[1])
        graphs[graph_pos[conn[0]]].output_dists.append(conn[2])

        # bi-directional
        graphs[graph_pos[conn[1]]].outputs.append(conn[0])
        graphs[graph_pos[conn[1]]].output_dists.append(conn[2])

    #############################

    dist = {}
    prev = {}
    Q = []
    for node_id in node_ids:
        dist[node_id] = np.inf
        prev[node_id] = np.nan
        Q.append(node_id)
    dist[source] = 0
    dist[target] = np.inf

    while len(Q) > 0:
        dist_in_Q = {k:dist[k] for k in dist if k in Q}
        u = min(dist_in_Q,key=dist_in_Q.get)

        Q.remove(u)

        for idx in range(len(graphs[graph_pos[u]].outputs)):
            v = graphs[graph_pos[u]].outputs[idx]
            alt = dist[u] + graphs[graph_pos[u]].output_dists[idx]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    path = []
    u = target
    if dist[u] != np.inf:
        path.append(u)
        while True:
            path.append(prev[u])
            u = prev[u]
            if u == source:
                break
    path.reverse()
    print(f'shortest path: {path}')

#################################################################################
#################################################################################

class node():
    def __init__(self,id):
        self.id = id
        self.outputs = []
        self.output_dists = []

#################################################################################
#################################################################################

if __name__ == '__main__':
    main()
