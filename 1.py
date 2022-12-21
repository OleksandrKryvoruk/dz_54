import networkx as nx
import matplotlib.pyplot as plt

with open('cities.csv', "r") as file:
    all_words = []
    for line in file:
        a = file.readline()
        x = a.replace('\n', '').split(";")
        all_words.append(x)

g = nx.Graph()
for city in all_words:
    g.add_edge(city[0], city[1], weight = city[2])

print(nx.shortest_path(g, 'Kyiv', 'Lviv', weight=''))
print(nx.shortest_path_length(g, 'Kyiv', 'Lviv', weight=''))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Graph Generation")

nx.draw_networkx(g)
plt.show()
