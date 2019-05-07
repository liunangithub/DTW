# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class BiNode:
    def __init__(self,element):
        self.element=element
        self.lchild=None
        self.rchild=None
    def get_element(self):
        return self.element
    def dic_form(self):
        dic_set={
                "element":self.element,
                "left":self.lchild,
                "right":self.rchild,
                }
        return dic_set
    def _str_(self):
        return str(self.element)
class BiTree:
    def __init__(self,tree_node=None):
        self.root=tree_node
    def add_node_in_order(self,element):
        node=BiNode(element)
        
        if self.root is None:
            self.root=node
        else:
            node_queue=list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node=node_queue.pop(0)
                if q_node.lchild is None:
                    q_node.lchild = node
                    break
                elif q_node.rchild is None:
                    q_node.rchild = node
                    break
                else:
                    node_queue.append(q_node.lchild)
                    node_queue.append(q_node.rchild)
    def set_up_in_order(self,element_list):
        for elements in element_list:
            self.add_node_in_order(element)

                        
"""
class Tree:
    def _init_(self):
        self.root=None
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
        else:
            q=[self.root]
            
            while True:
                pop_node=q.pop(0)
                if pop_node
                
                
                
                 def traversal_create(self,root):
        data=input()
        if data =='a':
            return None
        else:
            root.data=data
            root.lchild=self.traversal_create(root.lchild)
            root.rchild=self.traversal_create(root.rchild)
            return root
print(BiTree.traversal_create())
    
"""

    


