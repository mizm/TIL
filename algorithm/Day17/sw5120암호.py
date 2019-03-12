class Node :
	def __init__(self,data,link=None,pre=None):
		self.data = data
		self.link = link
		self.pre = pre


def Enqueue(item) :
	global head
	newNode = Node(item)
	if head == None :
		head = newNode
	else :
		p = head
		while p.link :
			if p.link == head:
				break
			p = p.link
		newNode.link = head
		newNode.prelink = p
		p.link = newNode

for tc in range(int(input())) :
	n,m,k = map(int,input().split())
	head = None
	for i in list(map(int,input().split())) :
		Enqueue(i)
	time = 0
	cnt = 0
	p = head

	while p :
		if time == k :
			break
		cnt += 1
		p = p.link
		if cnt % m == m-1 :
			new = Node((p.data+p.link.data))
			new.link = p.link
			p.link.pre = new
			new.pre = p
			p.link = new
			time += 1
	p = head
	cnt = 0
	print('#%d '%(tc+1),end='')
	while p :
		# print(p.data)
		if p.link == head :
			cnt = 0
			while p :
				if cnt > 9 :
					break
				if p == head:
					print(p.data,end=' ')
					break
				print(p.data,end= ' ')
				p = p.pre
				cnt+=1
			break
		p.link.pre = p
		p = p.link
	print()



