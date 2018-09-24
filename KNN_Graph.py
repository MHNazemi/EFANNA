

class Graph:
    def __init__(self, trees=None, points=None, depth=None):
        """ns  = nodes
        ts  =  trees
        ps  = points
        d = depth"""
        self.ns = []
        self.ts = trees
        self.ps = points
        self.d = depth

    def create(self):
        self.g = self.__CreateGraph()
        return self.g

    def __CreateGraph(self):
        g_res = Graph()
        for p_ in self.ps:
            g_tmp = Graph()
            for t_ in self.ts:

                # depth first search to first leaf d = depth   l = leaf ?
                def dfs(d, t, l=True):
                    d_ = 0
                    n_ = t.root

                    if l:
                        while not n_.l:
                            d_ = d_ + 1
                            if n_.v >= p_[n_.d]:
                                n_ = n_.c_l
                            else:
                                n_ = n_.c_r
                        return n_, d_
                    else:
                        while d_ < d and not n_.l:
                            d_ = d_ + 1
                            if n_.v >= p_[n_.d]:
                                n_ = n_.c_l
                            else:
                                n_ = n_.c_r
                        return n_

                leaf, depth = dfs(None, t_)
                # ??? add to list
                g_tmp.ns.append(leaf.ps)

                depth = depth - 1
                while depth < self.d:
                    node = dfs(depth, t_, False)
                    if not node.l:
                        if node.v >= p_[node.d] and node.c_l != None:
                            node = node.c_r
                            leaf = dfs(node, t_, True)
                            # ??? add to list
                        elif node.v < p_[node.d] and node.c_r != None:
                            node = node.c_l
                            leaf = dfs(node, t_, True)
                            # ??? add to list
                        else:
                            # ??? add to list
                            pass
                    else:
                        # ??? add to list
                        pass

                    depth = depth - 1
            # check the top k of closest
            # add list to graph

        # return Graph
        return ''


class Node:
    def __init__(self):
        # nn = neighbours
        self.nn = []
        self.value = None
