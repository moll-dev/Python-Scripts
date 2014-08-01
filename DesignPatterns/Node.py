class Node:
	def __init__(self, parent):
		if parent is None:
			self.isRoot = True
		else:
			self.isRoot = False
			self.parent = parent
			self.parent.add_child(self)

		self.children = []

	def __str__(self):
		return 'Node'

	def add_child(self, child):
		self.children.append(child)

	def print_tree_below(self, tabs = 0):
		string = ''
		print self
		for child in self.children:
			if child.children == []:
				print tabs*'\t'+ str(child)
			else:
				child.print_tree_below(tabs+1)

n1 = Node(None)
n2 = Node(n1)
n3 = Node(n1)

n4 = Node(n2)
n5 = Node(n2)

n1.print_tree_below()
