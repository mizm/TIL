n = int(input())
item = []
k = 0
for i in range(n) :
	item.append(list(map(int,input().split())))
base = 1
while base < n : base<<=1

idt = [[] for i in range (base<<1)]
item = sorted(item)
for k in range(n):
	idt[base+k].append(k)
brlist = []
for i in range(base-1,0,-1) :
	la = len(idt[i*2])
	lb = len(idt[i*2+1])
	if la > 0 and lb > 0 :
		if item[idt[i*2][la-1]][1] < item[idt[i*2+1][0]][1] :
			idt[i].extend(idt[i*2]+idt[i*2+1])
		else :
			idt[i].extend(idt[i*2+1])
			brlist.extend(idt[i*2])
	if la > 0 and lb == 0 :
		idt[i].extend(idt[i*2])
	elif la == 0 and lb > 0 :
		idt[i].extend(idt[i*2+1])
print(idt)
print(n-len(idt[1]))
for i in sorted(brlist) :
	print(item[i][0])