#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BTNode:
    def __init__(self,d,l,r):
        self.data = d
        self.left = l
        self.right = r
          
    def updateChild(self, oldChild, newChild):
        if self.left == oldChild:
            self.left = newChild
        elif self.right == oldChild:
            self.right = newChild
        else: raise Exception("updateChild error")

    # prints the node and all its children in a string
    def __str__(self):  
        st = str(self.data)+" -> ["
        if self.left != None:
            st += str(self.left)
        else: st += "None"
        if self.right != None:
            st += ", "+str(self.right)
        else: st += ", None"
        return st + "]"
    
class Queue:
    def __init__(self):
        self.inList = LinkedList()

    def __str__(self):
        return str(self.inList)
        
    def size(self):
        return self.inList.length

    def enq(self, e):
        self.inList.append(e)

    def deq(self):
        return self.inList.remove(0)

class Node:
    def __init__(self, d, n):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        st = "--> "
        ptr = self.head
        while ptr != None:
            st = st + str(ptr.data)
            st = st+" -> "
            ptr = ptr.next
        return st+"None"
        
    def search(self, d):
        i = 0
        ptr = self.head
        while ptr != None:
            if ptr.data == d:
                return i
            ptr = ptr.next
            i += 1
        return -1
        
    def append(self, d):
        if self.head == None:      
            self.head = Node(d,None) 
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(d,None)
        self.length += 1

    def insert(self, i, d):
        if self.head == None or i == 0:
            self.head = Node(d,self.head)
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            ptr.next = Node(d,ptr.next)
        self.length += 1

    def remove(self, i): # removes i-th element and returns it
        if self.head == None:
            return None
        if i == 0:
            val = self.head.data
            self.head = self.head.next
            self.length -= 1
            return val
        ptr = self.head
        while i>1 and ptr.next != None:
            ptr = ptr.next
            i -= 1
        if i == 1:
            val = ptr.next.data
            ptr.next = ptr.next.next
            self.length -= 1
            return val
    
    def removeVal(self, d):
        if self.head == None:
            return
        if self.head.data == d:
            self.head = self.head.next
            self.length -= 1
        else:
            ptr = self.head	
            while ptr.next != None:
                if ptr.next.data == d:
                    ptr.next = ptr.next.next
                    self.length -= 1
                    break
                ptr = ptr.next
    
    def sublist(self, i):
        ptr = self.head
        ls = LinkedList()
        ls.length = self.length
        while ptr != None and i>0:
            ptr = ptr.next
            i -= 1
            ls.length -= 1
        ls.head = ptr
        return ls


class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __str__(self):
        return str(self.root)

    def search(self, d):   
        ptr = self.root
        while ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False    
    
    def add(self, d):
        if self.root == None:
            self.root = BTNode(d,None,None)
        else:
            ptr = self.root
            while True:
                if d < ptr.data:
                    if ptr.left == None:
                        ptr.left = BTNode(d,None,None)
                        break
                    ptr = ptr.left
                else:
                    if ptr.right == None:
                        ptr.right = BTNode(d,None,None)
                        break
                    ptr = ptr.right
        self.size += 1
    
    def count(self, d):
        ptr = self.root
        count = 0
        while ptr != None:
            ptr = self._searchNode(ptr,d)
            if ptr != None:
                count += 1
                ptr = ptr.right
        return count

    def _searchNode(self, ptr, d):
        while ptr != None:
            if d == ptr.data:
                return ptr
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return None
    
    def remove(self,d):
        if self.root == None: return
        if self.root.data == d: 
            self.size -= 1
            return self._removeRoot()
        parentPtr = None
        ptr = self.root
        while ptr != None and ptr.data != d:
            parentPtr = ptr                
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        if ptr != None:
            self.size -= 1
            self._removeNode(ptr,parentPtr)
            
    # removes the node ptr from the tree altogether
    def _removeNode(self, ptr, parentPtr):
        # there are 3 cases to consider:
        # 1. the node to be removed is a leaf (no children)
        if ptr.left == ptr.right == None:
            parentPtr.updateChild(ptr,None)
        # 2. the node to be removed has exactly one child            
        elif ptr.left == None:
            parentPtr.updateChild(ptr,ptr.right)
        elif ptr.right == None:
            parentPtr.updateChild(ptr,ptr.left)
        # 3. the node to be removed has both children
        else:
            parentMinNode = ptr
            minNode = ptr.right
            while minNode.left != None:
                parentMinNode = minNode
                minNode = minNode.left
            # bypass the min node
            parentMinNode.updateChild(minNode,minNode.right)
            # and replace the ptr node with the min node
            parentPtr.updateChild(ptr,minNode)
            minNode.left = ptr.left
            minNode.right = ptr.right
        
    def _removeRoot(self):
        # this is essentially a hack: we are adding a dummy node at 
        # the root and call the previous method -- it allows us to
        # re-use code
        parentRoot = BTNode(None,self.root,None)
        self._removeNode(self.root,parentRoot)
        self.root = parentRoot.left

    # removes the root node from the tree altogether (directly)
    def _removeRoot2(self):
        ptr = self.root
        # there are 3 cases to consider:
        # 1. the root is a leaf (no children)
        if ptr.left == ptr.right == None:
            self.root = None
        # 2. the root has exactly one child            
        elif ptr.left == None:
            self.root = ptr.right
        elif ptr.right == None:
            self.root = ptr.left
        # 3. the root has both children
        else:
            parentMinNode = ptr
            minNode = ptr.right
            while minNode.left != None:
                parentMinNode = minNode
                minNode = minNode.left
            parentMinNode.updateChild(minNode,minNode.right)
            minNode.left = ptr.left
            minNode.right = ptr.right
            self.root = minNode
            
    def min(self):
        ptr = self.root
        while ptr.left != None:
            ptr = ptr.left
        return (ptr.data)
    
    def _sumAllRec(self, ptr):
        if ptr == None:
            return 0
        return (ptr.data + self._sumAllRec(ptr.left) + self._sumAllRec(ptr.right))
    
    def sumAll(self):
        ptr = self.root
        return self.sumAllAux(ptr)
    
    def sumAllAux(self, ptr):
        if ptr == None:
            return 0
        return (ptr.data + self.sumAllAux(ptr.left) + self.sumAllAux(ptr.right))
    
    def sumAllBFS(self):
        q = Queue()
        q.enq(self.root)
        sum = 0
        while q.size() > 0:
            ptr = q.deq()
            if ptr == None:
                continue
            sum += ptr.data
            q.enq(ptr.left)
            q.enq(ptr.right)
        return sum
    
    def toSortedArray(self):
        A = []
        ptr = self.root
        return self.toSortedArrayAux(A, ptr)
    
    def toSortedArrayAux(self, A, ptr):
        if ptr == None: return
        if ptr:
            self.toSortedArrayAux(A,ptr.left)
            A.append(ptr.data)
            self.toSortedArrayAux(A,ptr.right)
        return A
    
    
def inOrderPrint(t):
        if t == None:
            return
        
        inOrderPrintAux(t.left)
        print(t.data)
        inOrderPrintAux(t.right)

    

A = BST()
A.add(42)
A.add(21)
A.add(40)
A.add(3)
A.add(56)
A.add(99)
A.add(58)
A.add(21)
A.add(46)
A.add(49)

print(A.min())
print(A._sumAllRec(A.root))
print(A.sumAll())
print(A.sumAllBFS())
print("")
print(inOrderPrint(A))
print(A.toSortedArray())


# In[3]:


class BSTQueue:
    def __init__(self):
        self.root = None
        self.queue = Queue()
        self.size = 0
    
    def enq(self, d):
        self.queue.enq(d)
        if self.root == None:
            self.root = BTNode(d,None,None)
        else:
            ptr = self.root
            while True:
                if d < ptr.data:
                    if ptr.left == None:
                        ptr.left = BTNode(d,None,None)
                        break
                    ptr = ptr.left
                else:
                    if ptr.right == None:
                        ptr.right = BTNode(d,None,None)
                        break
                    ptr = ptr.right
        self.size += 1
    
    def deq(self):
        self.queue.deq()
        ptr = self.root
        if ptr == None:
            return
        # there are 3 cases to consider:
        # 1. the root is a leaf (no children)
        if ptr.left == ptr.right == None:
            self.root = None
        # 2. the root has exactly one child            
        elif ptr.left == None:
            self.root = ptr.right
        elif ptr.right == None:
            self.root = ptr.left
        # 3. the root has both children
        else:
            parentMinNode = ptr
            minNode = ptr.right
            while minNode.left != None:
                parentMinNode = minNode
                minNode = minNode.left
            parentMinNode.updateChild(minNode,minNode.right)
            minNode.left = ptr.left
            minNode.right = ptr.right
            self.root = minNode
        self.size -= 1
    
    def search(self,d):
        ptr = self.root
        while ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False
    
    def count(self, d):
        ptr = self.root
        count = 0
        while ptr != None:
            if d == ptr.data:
                count += 1
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return count

A = BSTQueue()
A.enq(42)
A.enq(21)
A.enq(40)
A.enq(3)
A.enq(56)
A.enq(99)
A.enq(58)
A.enq(21)
A.enq(46)
A.enq(49)
A.deq()
print(A.count(46))
A.deq()
print(A.size)
print(A.search(21))
print(A.count(21))
print(A.queue)


# In[ ]:




