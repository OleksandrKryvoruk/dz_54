import networkx as nx

citylist = [['Mannheim', 'Frankfurt', 85], ['Mannheim', 'Karlsruhe', 80], ['Erfurt', 'Wurzburg', 186],
            ['Munchen', 'Numberg', 167], ['Munchen', 'Augsburg', 84], ['Munchen', 'Kassel', 502],
            ['Numberg', 'Stuttgart', 183], ['Numberg', 'Wurzburg', 103], ['Numberg', 'Munchen', 167],
            ['Stuttgart', 'Numberg', 183], ['Augsburg', 'Munchen', 84], ['Augsburg', 'Karlsruhe', 250],
            ['Kassel', 'Munchen', 502], ['Kassel', 'Frankfurt', 173], ['Frankfurt', 'Mannheim', 85],
            ['Frankfurt', 'Wurzburg', 217], ['Frankfurt', 'Kassel', 173], ['Wurzburg', 'Numberg', 103],
            ['Wurzburg', 'Erfurt', 186], ['Wurzburg', 'Frankfurt', 217], ['Karlsruhe', 'Mannheim', 80],
            ['Karlsruhe', 'Augsburg', 250], ['Mumbai', 'Delhi', 400], ['Delhi', 'Kolkata', 500],
            ['Kolkata', 'Bangalore', 600], ['TX', 'NY', 1200], ['ALB', 'NY', 800]]

g = nx.Graph()
for city in citylist:
    g.add_edge(city[0], city[1], weight = city[2])

def route(city_1, city_2):
    weight = 'weight'
    mar = nx.shortest_path(g, city_1, city_2, weight)
    len_1 = nx.shortest_path_length(g, city_1, city_2, weight)
    return mar, len_1

marsh, length = route('Numberg', 'Frankfurt')
print(marsh)
print(length)
nx.draw_networkx(g)
