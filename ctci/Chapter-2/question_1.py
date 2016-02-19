# how to create a linkedlist
# write code to remove duplicates from an unsorted linked list
# reference: http://alextrle.blogspot.com/2011/05/write-linked-list-in-python.html

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
List.add_node(2)
List.add_node(4)

def deleteDups(linkedlist):
	# if head is not empty... for each node:
	if linkedlist.head != None:
		node = linkedlist.head
		# create a dict for values
		value_dict = {node.data: True}

		node = node.next

	# while queue is not empty, add the current node's value to our dict
	while node.next != None: 
		value_dict[node.data] = True

	# for each node after 'head', check if value is in dict, if so, then move the node's next pointer to the next-next node
		if node.next.data in value_dict:
			node.next = node.next.next
		
		prev_node = node # remember your previous node, needed for last node check
		node = node.next # moves onto the next node to examine in our linked list
			

	# check if last node is duplicate	
	else:
		if node.data in value_dict:
			#print "last duplicate"
			prev_node.next = None


List.print_list()
deleteDups(List)
print "finished running deleteDups"
List.print_list()











