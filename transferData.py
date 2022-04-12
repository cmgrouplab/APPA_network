import numpy as np

#files = [f"data1/network{i}.txt" for i in range(1, 2)]
#networks = np.zeros((238, 238))
#networkData = []
# for ff in files:
network = np.loadtxt(
    "Network_data/Poisson_1_Yu/voronoi_connectivity_matrix.txt")
#networks += network

networkData = np.array(np.where(np.triu(network))).T


np.savetxt('poisson_voronoi_connectivity.txt',
           networkData, fmt='%i', delimiter=',')
