# partition linkedlist around x, all values less than x go in front, all values larger than x go in back

# input: 1, 6, 8, 2, 9
# x = 7
# output: 1, 6, 2, 8, 9 

# question: do I know where the xth node is?

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
List.add_node(8)
List.add_node(6)

# x = 7

def partition_me(x, linkedlist):

	# make less than x list
	Less_than_x = LinkedList()
	
	# make greater than x list
	greater_than_x = LinkedList()

	node = linkedlist.head


	while node.next != None: # so why While and not If?
		if node.data > x:
			greater_than_x.add_node(node.data)
		else:
			Less_than_x.add_node(node.data)
		node = node.next
	else:
		# last node
		if node.data > x:
			greater_than_x.add_node(node.data)
		else:
			Less_than_x.add_node(node.data)

	
	# after done adding to the less and greater than lists, put the two lists together
	# set last node of the "less" list to point to head of greater than list

	less_than_x_node = Less_than_x.head

	while less_than_x_node.next != None:
		less_than_x_node = less_than_x_node.next 
	else:
		less_than_x_node.next = greater_than_x.head

	print_me_node = Less_than_x.head
	
	while print_me_node != None:
		print print_me_node.data
		print_me_node = print_me_node.next



partition_me(7, List)

# another method using fast and slow nodes

def partition_alt(x, linkedlist):
	if linkedlist.head != None:
		p1 = linkedlist.head
		p2 = linkedlist.head.next

		while p2 != None:
			if p2.data < x:
				p1.next = p2.next #keeps track of the next node
				#print "p1.next: " + str(p1.next.data)

				p2.next = linkedlist.head # causes the "1 8"
				#print "p2.next " + str(p2.next.data)

				linkedlist.head = p2 # causes the 6
				print "linkedlist.head " + str(linkedlist.head.data)

				p2 = p1.next #after nodes are shifted, continue on the linkedlist
				#print "p2 " + str(p2.data)
			else:
				print "else"
				p1 = p1.next
				p2 = p2.next

	# print out sorted list
	print_node = linkedlist.head
	while print_node != None:
		print print_node.data
		print_node = print_node.next 

# create a linked list 
list_two = LinkedList()
list_two.add_node(1)
list_two.add_node(8) 
list_two.add_node(6) 
list_two.add_node(2)

partition_alt(7, list_two) # 2618






