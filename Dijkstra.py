# -*- coding: utf-8 -*-
"""
@author: t.maybour
"""

import numpy as np

#################################################################################
#################################################################################

def main():


    #############################
    # set up

    conns = [
        [0,1,1],
        [1,3,2],
        [0,2,1],
        [2,3,1]
    ]

    node_ids = list(set([x[0] for x in conns]+[x[1] for x in conns]))

    graphs = []
    graph_pos = {}
    for node_id in node_ids:
        graphs.append(node(node_id))
        graph_pos[node_id] = len(graphs)-1

    for conn in conns:
        graphs[graph_pos[conn[0]]].outputs.append(conn[1])
        graphs[graph_pos[conn[0]]].output_dists.append(conn[2])
        graphs[graph_pos[conn[1]]].inputs.append(conn[0])
        graphs[graph_pos[conn[1]]].input_dists.append(conn[2])

    source = 0
    target = 3

    #############################

    dist = {}
    prev = {}
    Q = []
    for node_id in node_ids:
        dist[node_id] = np.inf
        prev[node_id] = np.nan
        Q.append(node_id)
    dist[0] = 0

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
    path.append(u)
    while True:
        path.append(prev[u])
        u = prev[u]
        if u == source:
            break
    path.reverse()
    print(path)

#################################################################################
#################################################################################

class node():
    def __init__(self,id):
        self.id = id
        self.inputs = []
        self.input_dists = []
        self.outputs = []
        self.output_dists = []
    def __str__(self):
        return f'''
            id: {self.id},
            outputs: {self.outputs},
            output_dists: {self.output_dists},
            inputs: {self.inputs},
            input_dists: {self.input_dists}            
        '''

#################################################################################
#################################################################################

if __name__ == '__main__':
    main()