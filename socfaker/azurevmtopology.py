import matplotlib.pyplot as plt
import networkx as nx
from .azureproperties import AzureProperties
from .baseclass import BaseClass


class AzureVMTopology(BaseClass):

    def __init__(self):
        super(AzureVMTopology, self).__init__()
        self.root_node = ''
        self.graph = nx.Graph()
        self.props = AzureProperties()

    def __generate_topology_template(self, children_count=1):
        return_list = []
        parent = {}
        parent['root'] = {
            "location": self.props.location, 
            "network_zones": self.props.network_zone, 
            "score": self.props.score, 
            "id": "/subscriptions/{resource_group_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{vm_name}".format(
                resource_group_id=self.props.resource_group_id, 
                resource_group_name=self.props.resource_group_name, 
                vm_name=self.props.vm_name), 
            "severity": "Healthy"
        }
        child_list = []
        child_list.append({
            "1": "/subscriptions/{resource_group_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{vm_name}/subnets/default".format(
                resource_group_id=self.props.resource_group_id, 
                resource_group_name=self.props.resource_group_name, 
                vm_name=self.props.vm_name)
        })
        parent['children'] = child_list
        return_list.append(parent)

        parent = {}
        parent['root'] = {
            "location": self.props.location, 
            "network_zones": self.props.network_zone, 
            "score": self.props.score, 
            "id": "/subscriptions/{resource_group_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{vm_name}/subnets/default".format(
                resource_group_id=self.props.resource_group_id, 
                resource_group_name=self.props.resource_group_name, 
                vm_name=self.props.vm_name), 
            "severity": "High"
        }
        count = 1
        child_list = []
        while children_count <= count:
            child_dict = {}
            child_dict[count] = {
                "location": self.props.location, 
                "network_zones": AzureProperties().network_zone, 
                "score": AzureProperties().score, 
                "id": "/subscriptions/{resource_group_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{child_vm_name}".format(
                    resource_group_id=self.props.resource_group_id, 
                    resource_group_name=self.props.resource_group_name, 
                    child_vm_name=AzureProperties().vm_name), 
                "severity": "High"
            }
            child_list.append(child_dict)
            count += 1
        parent['children'] = child_list
        return_list.append(parent)
        return return_list


    def __parse_topology(self, topology):
        root = True
        for item in topology:
            if 'root' in item:
                count = 1
                item_id = item['root']['id'].rsplit('/',1)[1]
                self.graph.add_node(
                    item_id, 
                    weight=count, 
                    id=item['root']['id'], 
                    location=item['root']['location'], 
                    network_zones=item['root']['network_zones'], 
                    score=item['root']['score'], 
                    severity=item['root']['severity'])
                count += 2
                if root:
                    self.root_node = item_id
                    root = False

                for child in item['children']:
                    for key,val in child.iteritems():
                        if isinstance(val, dict):
                            self.graph.add_node(
                                val['id'].rsplit('/',1)[1], 
                                weight=count,id=val['id'], 
                                location=val['location'], 
                                network_zones=val['network_zones'], 
                                score=val['score'], 
                                severity=val['severity'])
                            self.graph.add_edge(item_id, val['id'].rsplit('/',1)[1])
                        else:
                            self.graph.add_edge(item_id, val.rsplit('/',1)[1])
                
    def get(self):
        return self.__generate_topology_template(children_count=self.random.randint(1,5))

    def topology_graphic(self, topology=None):
        if not topology:
            topology = self.__generate_topology_template(children_count=self.random.randint(1,5))
        self.__parse_topology(topology)
        pos = self.__hierarchy_pos(self.graph, root=self.root_node)

        fig = plt.figure(figsize=(15,4))
        color_map = []
        for node in self.graph:
            if node == self.props.vm_name:
                color_map.append('red')
            else:
                color_map.append('skyblue')

        nx.draw(
            self.graph, 
            pos=pos, 
            node_color=color_map, 
            node_size=2000, 
            edge_color='white', 
            font_color='white', 
            font_size=8)
        fig.set_facecolor("#00000F")

        plt.autoscale()

        for key, val in pos.iteritems():
            x,y = val
            plt.text(x,y-0.1,s=key, bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
        plt.savefig('image.png', facecolor=fig.get_facecolor(), bbox_inches='tight')
                

    def __hierarchy_pos(self, G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
        '''
        From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
        Licensed under Creative Commons Attribution-Share Alike 

        If the graph is a tree this will return the positions to plot this in a 
        hierarchical layout.

        G: the graph (must be a tree)

        root: the root node of current branch 
        - if the tree is directed and this is not given, 
        the root will be found and used
        - if the tree is directed and this is given, then 
        the positions will be just for the descendants of this node.
        - if the tree is undirected and not given, 
        then a random choice will be used.

        width: horizontal space allocated for this branch - avoids overlap with other branches

        vert_gap: gap between levels of hierarchy

        vert_loc: vertical location of root

        xcenter: horizontal location of root
        '''
        if not nx.is_tree(G):
            raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

        if root is None:
            if isinstance(G, nx.DiGraph):
                root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
            else:
                root = self.random.choice(list(G.nodes))

        def _hierarchy_pos(
            G, 
            root, 
            width=1., 
            vert_gap = 0.2, 
            vert_loc = 0, 
            xcenter = 0.5, 
            pos = None, 
            parent = None):
            '''
            see hierarchy_pos docstring for most arguments

            pos: a dict saying where all nodes go if they have been assigned
            parent: parent of this branch. - only affects it if non-directed

            '''

            if pos is None:
                pos = {root:(xcenter,vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)  
            if len(children)!=0:
                dx = width/len(children) 
                nextx = xcenter - width/2 - dx/2
                for child in children:
                    nextx += dx
                    pos = _hierarchy_pos(
                        G,child, 
                        width = dx, 
                        vert_gap = vert_gap, 
                        vert_loc = vert_loc-vert_gap, 
                        xcenter=nextx,
                        pos=pos, 
                        parent = root)
            return pos

        return _hierarchy_pos(
            G, 
            root, 
            width, 
            vert_gap, 
            vert_loc, 
            xcenter)
