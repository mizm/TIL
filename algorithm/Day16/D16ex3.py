class Node :
	def __init__(self,data,link=None):
		self.data = data
		self.link = link

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.link=node2
node2.link=node3
node3.link=node4
node4.link=node5

head = None
def Enqueue(item) :
	global head
	newNode = Node(item)
	if head == None :
		head = newNode
	else :
		p = head
		while p.link :
			if p.link.data > item :
				newNode.link = p.link
				p.link = newNode
				return
			p = p.link
		p.link = newNode


Enqueue(1)
Enqueue(5)
Enqueue(2)
Enqueue(4)
Enqueue(3)

p = head
while p :
	print(p.data)
	p = p.link
