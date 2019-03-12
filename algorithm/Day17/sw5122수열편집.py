class Node :
	def __init__(self,data,link=None):
		self.data = data
		self.link = link
def setlist(item) :
	global head
	new = Node(item)
	if not head :
		head = new
	else :
		p = head
		while p.link :
			p = p.link
		p.link = new
def insert(item,idx) :
	global head
	if idx == 0 :
		head = Node(item,head)
		return
	cnt = 0
	p = head
	while p :
		if cnt+1 == idx :
			p.link = Node(item,p.link)
		p = p.link
		cnt += 1
def delete(idx) :
	global head
	if idx == 0 :
		head = head.link
	cnt = 0
	p = head
	while p :
		if cnt+1 == idx :
			p.link = p.link.link
			break
		p = p.link
		cnt+=1
def edit(item,idx) :
	global head
	cnt = 0
	p = head
	while p :
		if cnt == idx :
			p.data = item
			break
		p=p.link
		cnt+=1
for tc in range(int(input())):
	n,m,l = map(int,input().split())
	head = None
	for i in list(map(int,input().split())) :
		setlist(i)
	Data = []
	for i in range(m) :
		Data.append(input().split())
	for i in Data :
		if i[0] == 'I' :
			insert(int(i[2]),int(i[1]))
		elif i[0] == 'D' :
			delete(int(i[1]))
		elif i[0] == 'C' :
			edit(int(i[2]),int(i[1]))
		p = head
		# while p:
		# 	print(p.data)
		# 	p = p.link
	cnt = 0
	p = head
	result = -1
	while p:
		# print(p.data)
		if cnt == l:
			result = p.data
			break
		cnt += 1
		p = p.link
	print('#%d %d'%((tc+1),result))