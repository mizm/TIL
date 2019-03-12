class Node :
	def __init__(self,data,link=None,prelink=None):
		self.data = data
		self.prelink = prelink
		self.link = link
def setlist(head,idx,item) :        # f
	for i in item :
		new = Node(i)
		if not head :
			head = new
			tail[idx]=new
		else :
			p = tail[idx]
			# while p.link :
			# 	p = p.link
			p.link = new
			new.prelink = p
			tail[idx] = new
	return head

def insert(head1,head2,idx) :
	p1 = head1
	p2 = head2
	item = p2.data
	chkitem = p1.data
	if chkitem >= item :
		while p2 :
			# print(p2.data)
			if p2.link == None :
				p2.link = p1
				p1.prelink = p2
				return head2
			p2 = p2.link
		# return
	while p1 :
		if p1.data > item :
			break
		else :
			if p1.link == None :
				p1.link = p2
				p2.prelink = p1
				tail[0] = tail[idx]
				return head1
			p1 = p1.link
	pt = p1.prelink
	pt.link = p2
	p2.prelink = pt
	while p2:
		if p2.link == None :
			p2.link = p1
			p1.prelink=p2
			# tail[0] = tail[idx]
			return head1
		p2 = p2.link


for tc in range(int(input())):
	n,m = map(int,input().split())
	Data = [0]*m
	tail = [0]*m
	for i in range(m) :
		Data[i] = setlist(Data[i],i,list(map(int,input().split())))
	for i in range(1,m) :
		Data[0] = insert(Data[0],Data[i],i)
		# Data[0] = insert(Data[0],Data[2])
		# Data[0] = insert(Data[0],Data[3])
	# for i in range(m) :
	p = tail[0]
	print('#%d'%(tc+1),end=' ')
	cnt = 0
	while p:
		if cnt > 9 :
			break
		print(p.data,end=' ')
		p = p.prelink
		cnt+=1
	print()