class Node(object):
	def __init__(self,value,prev=None ,next=None):
		self.value = value
		self.prev = prev
		self.next = next

class  DoublyLinkedList(object):
	def __init__(self):		
		self.head = None
		self.tail = None		
		self.size = 0	 
	def addNode(self,value):
		if self.size == 0:			
			self.head = Node(value)
			self.tail = self.head			
		else:
			self.tail.next = Node(value,self.tail) 			
			self.tail = self.tail.next		
		self.size+=1	
		return self	
	def deleteNode(self,index):
		deletionNode = self.head	
		if index >=self.size or index < 0:
			print "out of bounds"
			return "out of bounds"						
		if index == 0:
			self.head = self.head.next
			self.head.prev = None
		elif index ==self.size-1:
			self.tail = self.tail.prev
			self.tail.next = None
		else:		
			for i in range(index):
				deletionNode = deletionNode.next		
			deletionNode.next.prev = deletionNode.prev
			deletionNode.prev.next = deletionNode.next
		self.size-=1	
		return self
	def insertAfter(self,value,index):
		insertLoc = self.head
		if index >=self.size or index < 0:
			print "out of bounds"
			return "out of bounds"	
		if index == 0:
			new_node = Node(value,None,self.head)
			self.head.prev = new_node
			self.head = new_node	
		elif index ==self.size-1:
			self.addNode(value)
		else:
			for i in range(index):
				insertLoc = insertLoc.next	
			new_node = 	Node(value,insertLoc,insertLoc.next)
			insertLoc.next.prev = new_node
			insertLoc.next =new_node
		self.size+=1
		return self	
	def display_list(self):
		loc = self.head		
		for i in range(self.size):
			print loc.value
			loc = loc.next
			
					


dList = DoublyLinkedList()
dList.addNode(1).addNode(2).addNode(3).addNode(4).addNode(5)
dList.deleteNode(2)
dList.insertAfter(22,2)
dList.display_list()
print "head" , dList.head.value
print "tail" , dList.tail.value





# class  DoublyLinkedList(object):
# 	def __init__(self):		
# 		self.prevNode =None
# 		self.nextNode=None		
# 		self.size = 0	 
# 	def addNode(self,value):
# 		if self.size == 0:			
# 			self.node = Node(value)	 
# 			self.prevNode = self.node
# 			self.nextNode = None
# 		else:			
# 			self.node = Node(value,self.prevNode,self.nextNode)
# 			self.prevNode = self.node
# 			self.nextNode = self.node
# 		self.size+=1	
# 		return self	
