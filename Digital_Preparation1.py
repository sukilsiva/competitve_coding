class routes:
    def __init__(self, routes):
        self.graph_dict = routes
    def get_path(self, start, end, path=[]):
        path = path + [start]
        paths = []
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return [] 

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths


def find_rich_poor_path(inputs,m,n):
    result = {}
    array = []
    for i in range(1,m+1):
        result[i] = 0
    for i in inputs:
        first = i[0]
        second = i[1]
        money = i[2]
        result[first] += money
        result[second] -= money 
        array.append((str(first), str(second)))
    result_dict = {key:value for key,value in sorted(result.items(), key= lambda item : item[1])}
    poor, rich = str(list(result_dict.keys())[0]), str(list(result_dict.keys())[-1])
    graph = {}
    for start, end in array:
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
    route_graph = routes(graph)
    paths = route_graph.get_path(rich, poor)
    length = 10000000
    for i in paths:
        if len(i)<length:
            length = len(i)
            shortest_path = i
    return list(map(int, shortest_path)) [::-1]
    

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    array = []
    for i in range(m):
        inpu = input()
        arr = list(map(int, inpu.split()))
        array.append(arr)
    print(find_rich_poor_path(array, m ,n))