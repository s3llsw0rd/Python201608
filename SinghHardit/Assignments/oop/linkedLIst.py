class Node(object):
	def __init__(self,value,prev=0,next=0):
		self.prev = prev
		self.next = next

class  DoublyLinkedList(Node):
	def __init__(self,head,tail):
		self.head = head
		self.tail = tail
	count = 0 
	def addNode(self,value,prev,next):
		super(DoublyLinkedList,self).__init__(1,count,count+1)	 
		
			
		

	


node1 = Node(1,0,0)
node2 = Node(2,1,0)			
node3 = 