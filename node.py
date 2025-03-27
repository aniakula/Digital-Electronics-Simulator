from enum import Flag, auto

class NodeType(Flag):
    OUT = auto()
    IN = auto()
    MID = auto()
    CUSTOM = auto()
    AND = auto()
    OR = auto()
    XOR = auto()
    NOT = auto()
    GATES = AND | OR | XOR | NOT


class Node:
    def __init__(self, type: NodeType, parents : [Node] = [], children : [Node] = [], value: bool = None):
        self.type = type
        self.value = value

        match type:
            case NodeType.CUSTOM:
                self.parents = parents
                self.children = children
            case NodeType.AND | NodeType.OR | NodeType.XOR:
                parents = [Node(NodeType.MID, children=[self]), Node(NodeType.MID, children=[self])]
                children = [Node(NodeType.MID, parents=[self])]
            case NodeType.NOT:
                parents = [Node(NodeType.MID, children=[self])]
                children = [Node(NodeType.MID, parents=[self])]
        

    def get_parents(self) -> [Node]: 
        return self.parents
    
    def get_children(self) -> [Node]:
        return self.children
    
    def get_value(self) -> bool:
        return self.value
    
    def set_value(self, value: bool):
        self.value = value
        return self.value
    
    def link(self, parent: Node, child: Node):
        if parent.type == (NodeType.IN | NodeType.MID) and child.type == (NodeType.OUT | NodeType.MID):
            parent.children.append(child)
            child.parents.append(parent)
        

    def run (self):
        match self.type:
            case NodeType.AND:
                self.children[0].set_value(self.parents[0] and self.parents[1])
                self.children.run()
            case NodeType.OR:
                self.children[0].set_value(self.parents[0].run() or self.parents[1].run())
            case NodeType.XOR:
                self.children[0].set_value(self.parents[0].run() != self.parents[1].run())
            case NodeType.NOT:
                self.children[0].set_value(not self.parents[0].run())
            case NodeType.CUSTOM:
                for c in self.children:
                    c.run()
            case NodeType.IN | NodeType.MID:
                self.children.set_value(self.value)
                self.children.run()    
            case NodeType.OUT:
                return


    def __str__(self):
        return str(self.value)