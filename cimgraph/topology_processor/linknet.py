import time
import json
import logging
import importlib

_log = logging.getLogger(__name__)

class LinkNet():
    def __init__(self, cim_profile, graph):
        self.cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)
        self.graph = graph
        self.NodeList = []
        self.TermList = []
        self.Feeders = {}
        self.Islands = {}

    # Builds LinkNet linked lists for all CIM classes specified by EqTypes
    def build_linknet(self, EqTypes):
        # Intialize counter objects
        index = 0
        counter = 0
        # Build __linknet_list__ for all specified CIM classes:
        for i0 in range(len(EqTypes)): 
            [index, counter] = self.build_class_lists(EqTypes[i0], index, counter)
        # Add floating nodes not connected to a branch:
        StartTime = time.perf_counter()
        AllNodes = list(self.graph[self.cim.ConnectivityNode].keys())
        ParsedNodes = []
        for node in self.NodeList:
            ParsedNodes.append(node.mRID)
        MissingNodes = list(set(AllNodes).difference(ParsedNodes))
        for i1 in range(len(MissingNodes)):
            node = self.graph[self.cim.ConnectivityNode][MissingNodes[i1]]
            try:
                getattr(node, '__linknet_list__')
            except:
                setattr(node, '__linknet_node__', index+1)
                setattr(node, '__linknet_list__', 0)
                index = index+1
                self.NodeList.append(node)
                
        _log.info("Processed " + str(len(MissingNodes)) + " missing nodes in " + str(round(1000*(time.process_time() - StartTime))) + " ms")
        # Dump JSON copies of base LinkNet structure. These are used to rebuild topo after each switch change
#         self.BaseConnDict = json.dumps(self.graph[self.cim.ConnectivityNode])
#         self.BaseTermDict = json.dumps(self.graph[self.cim.Terminal])
        _log.info("Processed " + str(len(MissingNodes)) + " missing nodes in " + str(round(1000*(time.perf_counter() - StartTime))) + " ms")

 # Build LinkNet structure for single CIM equipment type, called by build_linknet()
    # Three-winding transformers not yet supported
    def build_class_lists(self, eqtype, index, old_counter):
        i2 = -1
        index2 = 0
        if eqtype not in self.graph:
            return index, old_counter
        StartTime = time.perf_counter()
        EquipKeys = list(self.graph[eqtype].keys())

        for device in self.graph[eqtype].values():
            i2 = 0
            # Identify nodes and terminals for readability
            term1=getattr(device, "Terminals")[0]
            node1=term1.ConnectivityNode
            # If node1 not in LinkNet , create new keys
            try:
                getattr(node1, "__linknet_node__")
            except:
                setattr(node1, '__linknet_node__', index+1)
                setattr(node1, '__linknet_list__', 0)
                index = index+1
                self.NodeList.append(node1)

            # If two-terminal device, process both terminals
            if len(getattr(device, "Terminals")) == 2:
                # Identify nodes and terminals for readability
                term2=getattr(device, "Terminals")[1]
                node2=term2.ConnectivityNode
                # Create keys for new terminals
#                 self.graph[self.cim.Terminal][term2] = {}
#                 self.graph[self.cim.Terminal][term2]['ConnectivityNode'] = node2
                setattr(term1, '__linknet_term__', 2*i2+old_counter+1)
                setattr(term2, '__linknet_term__', 2*i2+old_counter+2)
                self.TermList.append(term2)
                # If node2 not in LinkNet , create new keys
                try:
                    getattr(node2, "__linknet_node__")
                except:
                    setattr(node2, '__linknet_node__', index+1)
                    setattr(node2, '__linknet_list__', 0)
                    index = index+1
                    self.NodeList.append(node2)

                # 1. Move node list variables to terinal next    
                setattr(term1, '__linknet_next__', getattr(node1, '__linknet_list__'))
                setattr(term2, '__linknet_next__', getattr(node2, '__linknet_list__'))
                # 2. Populate Terminal list far field with nodes
                setattr(term1, '__linknet_far__', getattr(node2, '__linknet_node__'))
                setattr(term2, '__linknet_far__', getattr(node1, '__linknet_node__'))
                # 3. Populate Connectivity nodes list with terminals
                setattr(node1,'__linknet_list__', getattr(term1,'__linknet_term__'))
                setattr(node2, '__linknet_list__', getattr(term2, '__linknet_term__'))
                index2 = index2 + 2
            # If one-terminal device, process only single terminal
            else:
                setattr(term1, '__linknet_term__', i2+(old_counter)+1)
                setattr(term1, '__linknet_next__', getattr(node1, '__linknet_list__'))
                setattr(term1, '__linknet_far__', getattr(node1, '__linknet_node__'))
                setattr(node1, '__linknet_list__', getattr(term1, '__linknet_term__'))
                index2 = index2 + 1

            _log.info("Processed " + str(i2+1) + ' ' + str(eqtype) + " objects in " + str(round(1000*(time.perf_counter() - StartTime))) + " ms")
        counter = old_counter+index2
        return index, counter
                   
    def spanning_tree(self, eqtype, RootKeys, Tree, Scope):
        root = ''
        TotalNodes=0
        old_len = len(Tree.keys())
        StartTime = time.process_time()

        
        for i6 in range(len(RootKeys)):
            root = RootKeys[i6]
            Tree[root] = []

            # If switch object, only use second node
            if eqtype in [self.cim.Breaker, self.cim.Fuse, self.cim.LoadBreakSwitch, self.cim.Recloser]:
                node2 = self.graph[eqtype][root].Terminals[1].ConnectivityNode
                [not_in_tree, found] = self.check_tree(node2, Tree, Scope, root)
                if not_in_tree:
                    Tree[root].append(node2)
                    FirstNode = 0
                    LastNode = 1 # only 1 node used, so initialize list at 0,1
            # If DER object, only has one node
            elif eqtype in [self.cim.SynchronousMachine, self.cim.PowerElectronicsConnection, self.cim.EnergySource]:
                #[not_in_tree, found] = self.check_tree(self.EquipDict[eqtype][root]['node1'], Tree, Scope, root)
               # if not_in_tree:
                node1 = self.graph[eqtype][root].Terminals[0].ConnectivityNode
                Tree[root].append(node1)
                FirstNode = 0 
                LastNode = 1 # only 1 node exists, so initialize list at 0,1
                #else:
                    
            # Otherwise, use both nodes    
            else: # Then 2-terminal object
                node1 = self.graph[eqtype][root].Terminals[0].ConnectivityNode
                node2 = self.graph[eqtype][root].Terminals[1].ConnectivityNode
                [not_in_tree, found] = self.check_tree(node2, Tree, Scope, root)
                if not_in_tree:
                    Tree[root].append(node1)
                    Tree[root].append(node2)
                    FirstNode = 1 
                    LastNode = 2 # 2 nodes in starting list, so initialize at 1,2
                else:
                    break
            while LastNode != FirstNode:
                NextTerm = getattr(Tree[root][FirstNode],'__linknet_list__')
                FirstNode = FirstNode + 1
                while NextTerm != 0:
                    # Get next node and terminal for current node
                    NextNode = getattr(self.TermList[NextTerm-1], '__linknet_far__')
                    NextTerm = getattr(self.TermList[NextTerm-1], '__linknet_next__')
                    node = self.NodeList[NextNode-1]
                    [not_in_tree, found] = self.check_tree(node, Tree, Scope, root)
                    # Add node if not in another tree        
                    if not_in_tree:       
                        try:
                            nomV = getattr(node.BaseVoltage, 'nominalVoltage')
                        except:
                            nomV = None
                        if nomV is not None:
                            # Stop building tree into sub-transmission network
                            if int(nomV) < 34000: 
                                Tree[root].append(self.NodeList[NextNode-1])
                                LastNode = LastNode + 1                       
                        else: # Add node to tree if no nominal voltage defined
                            Tree[root].append(self.NodeList[NextNode-1])
                            LastNode = LastNode + 1


            _log.info("Processed topology from  " + str(root) + ' with ' + str(len(Tree[root])) + " buses")

#         if root: self.log.info("Processed " + str(len(Tree.keys()) - old_len) + " topology trees containing " + str(TotalNodes+len(Tree[root])) + " buses in " + str(round(1000*(time.process_time() - StartTime))) + " ms")

        return Tree
    
    # function to check if a node is the spanning tree
    # use argument "all" to check all trees from all root nodes
    # use argument "single" to only check the single tree from current root node
    # node is ConnectivityNode mRID to be checked
    # root is used to specify "single" tree root key 
    def check_tree(self, node, Tree, Scope, root):
        not_in_tree = True
        found = 'False'
        if Scope == 'all': 
            TreeKeys = list(Tree.keys())
            for i7 in range(len(TreeKeys)):
                if node in Tree[TreeKeys[i7]]:
                    not_in_tree = False
                    found = TreeKeys[i7]
                    break
        else: 
            if node in Tree[root]: 
                not_in_tree = False
                found = root
        return not_in_tree, found
