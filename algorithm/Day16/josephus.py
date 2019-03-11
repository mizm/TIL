n=41
class Node :
	def __init__(self,data,link=None):
		self.data = data
		self.link = link
head = None
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
		p.link = newNode
for i in range(1,42) :
	Enqueue(i)

# cnt = 0
# p = head
# while p :
# 	if cnt > 90 :
# 		break
# 	print(p.data)
# 	cnt += 1
# 	p = p.link
p = head
cnt=0
r=41
while p :
	if r <= 2 :
		break
	pre = p
	cnt += 1
	p = p.link
	if cnt % 3 == 2 :
		print(p.data)
		r-=1
		cnt +=1
		if p == head:
			head = p.link
		pre.link = None
		p = p.link
		pre.link = p


print()
p = head
while r > 0 :
	r-=1
	print(p.data)
	p = p.link