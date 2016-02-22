# linked list code:
# node class: every node has a value and pointer to the next node
# when first instantiated, it has a value but is not pointed to any other node

class Node:
	def __init__(self, data):
		self.data = data # value
		self.next = None # pointer to the next node

# linked list class
class LinkedList:
# empty when first made (no nodes, head, or tail)
	def __init__(self):
		self.head = None
		self.tail = None
# functions to add/remove nodes and print list
	def add_node(self, data):
		# create node
		new_node = Node(data)

		# if no head, set new node as head
		if self.head == None:
			self.head = new_node

		# set last node's next pointer to the 'new' node
		if self.tail != None:
			self.tail.next = new_node # next was originally None, each node has a Next
			
		# set the new tail to the new node
		self.tail = new_node
		
	def remove_node(self, index):
		prev = None
		node = self.head # start at the beginning
		i = 0

		while (node != None) and (i < index): # traverse along the list
			prev = node 
			node = node.next
			i += 1 

		if prev == None: # None is default assignment at first
			self.head = node.next # when does this happen? if empty list?
		else:
			prev.next = node.next

	def print_list(self):
		#start at head and go through each node's next pointer until node is None
		node = self.head 
		while node != None:
			print node.data
			node = node.next

# create a linked list 
List = LinkedList()
List.add_node(1)
List.add_node(2)
List.add_node(3)
List.add_node(4)



def find_xth_to_last_node_v2(n, linkedlist):
	# create 2 pointers, p1 and p2 and set both to start of linkedlist
	p1 = linkedlist.head 
	p2 = linkedlist.head

	if linkedlist.head is None:
		print "error"

	else:
		# move p2 down n-1 times down linked list
		# return error message if n exceeds length of linked list
		for _ in range(n-1):
			if p2.next != None:
				p2 = p2.next
			else:
				print "n exceeds length of linkedlist"
		print "p2 is " + str(p2.data)
	# move p1 and p2 down until p2 hits end of list
	while p2.next != None:
		p2 = p2.next
		print p2.data
		p1 = p1.next

	# afterwards, return p1 value
	print p1.data


find_xth_to_last_node_v2(4, List)
find_xth_to_last_node_v2(0, List)
