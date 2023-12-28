class Graph:
    def __init__(self):
        self.graph = dict()
        self.num_nodes = 0
        self.str_graph = ''
        self.start_node = None

    def make_graph(self, inp):
        if self.graph:
            return
        for string in inp.split():
            self.num_nodes += 1
            lst = string.split(':')
            node = lst[0]
            ways = tuple(lst[1])
            self.graph[node] = ways
            self.str_graph += f"{node}: {','.join(ways)}\n"
            if self.num_nodes == 1:
                self.start_node = node

    def __repr__(self):
        return f"{self.graph!r}"

    def __str__(self):
        return self.str_graph

    @staticmethod
    def bfs(graph, start, end):
        queue = [start]
        visited = {start: None}
        while queue:
            cur_node = queue.pop(0)
            if cur_node == end:
                break
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    visited[next_node] = cur_node
                    queue.append(next_node)
        return visited

    def get_way(self, start, end):
        visited = self.bfs(self.graph, start, end)
        res = [start]
        cur_node = end
        while cur_node != start:
            res.insert(1, cur_node)
            cur_node = visited[cur_node]
        return res


if __name__ == '__main__':
    graph = Graph()
    inp = 'A:BC B:E C:ED E:D'
    graph.make_graph(inp)
    print(graph.get_way('A', 'D'))
    print(graph)
