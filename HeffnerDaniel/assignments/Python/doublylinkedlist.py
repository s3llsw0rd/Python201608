class Node(object):
	def __init__(self, data, prev = None, next = None):
		self.data = data
		self.next = next
		self.prev = prev

class DLList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def add_node(self, data):
		if self.head == None:
			new_node = Node(data, self, self)
			self.head = new_node
			self.tail = new_node
			return self
		else:
			new_node = Node(data, self.tail, self)
			self.tail.next = new_node
			self.tail = new_node
			return self
	def delete_node(self, data):
		x = self.get_node(data)
		if not x:
			print 'error: value not found in list'
		else:
			x.next.prev = x.prev
			x.prev.next = x.next
		return self
	def insert_node(self, data, data_before):
		if data_before == self:
			new_node = Node(data, self, self.head)
			self.head.prev = new_node
			self.head = new_node
			return self
		x = self.get_node(data_before)
		if not x:
			print 'error: value to insert data after not found in list'
		else:
			new_node = Node(data, x, x.next)
			x.next.prev = new_node
			x.next = new_node
		return self
	def print_values(self):
		x = self.head
		while x != self:
			print x.data
			x = x.next
	def get_node(self, data):
		x = self.head
		while x != self and x.data != data:
			x = x.next
		if x == self:
			return False
		else:
			return x

# Tests:
# LiLi = DLList()
# LiLi.add_node('first').add_node('second').add_node('third').add_node('fourth')
# LiLi.print_values()
# print '----------'
# LiLi.delete_node('third')
# LiLi.print_values()
# print '----------'
# LiLi.insert_node('third', LiLi).insert_node('fifth', 'second')
# LiLi.print_values()