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

for tc in range(int(input())):
	n,m,l = map(int,input().split())
	head = None
	for i in list(map(int,input().split())) :
		setlist(i)

	for i in range(m) :
		idx,item = map(int,input().split())
		insert(item,idx)
	p = head
	cnt = 0
	p = head
	while p:
		if cnt == l:
			print('#%d %d'%((tc+1),p.data))
			break
		cnt += 1
		p = p.link