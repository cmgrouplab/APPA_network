import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

files = [f"data1_0.3/network{i}.txt" for i in range(10, 10001, 100)]
# network_conn = []
# networkData = []
data = []
for ff in files:
    network = np.loadtxt(ff)
    # networks += network
    networks_authority = np.sum(network, axis=0, keepdims=True)
    data.append(networks_authority)

data = np.vstack(data)

rows, cols = np.where(data > 0.0015)
high_data = np.take(data, cols, axis=1)
plt.plot(high_data)
plt.savefig('high_authority.png')

plt.plot(data)
plt.savefig('authority_0.3.png')


# networks = np.loadtxt("data1_0.5/network10000.txt")
# cm = (networks > 0).astype(int)
# g = nx.from_numpy_matrix(cm)
# for i in range(len(networks)):
#     for j in range(len(networks[0])):
#         if networks[i][j] > 0:
#             network_conn.append([i, j, networks[i][j]])

# print(networks)
# print(len(g.edges))
# print(nx.density(g))
# print(nx.average_clustering(g))
# n = g.order()
# indegrees = dict(g.degree()).values()
# max_in = max(indegrees)
# centralization = float((n * max_in - sum(indegrees))) / (n-1)**2
# print(centralization)


#max_v = max(networks_authority)
#networks_authority = networks_authority / max_v
# print(networks_authority)
# red_index = np.where((networks_authority <=
#                      max_v) & (networks_authority >= 0.8 * max_v))
# print(networks)
# np.savetxt('networks_0.5_10000.txt',
#            network_conn, fmt='%0.7f', delimiter=',')
