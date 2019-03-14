def update(idx,item) :
	#idx,item
	idx += base-1
	idt[idx] = item
	while idx > 1 :
		idx >>= 1
		idt[idx] = idt[2*idx] + idt[2*idx + 1]
def RSQ(fr,to) :
	fr += base -1
	to += base -1
	re = 0
	while fr != to :
		if fr&1 :
			re+=idt[fr]
			fr+=1
		if not to&1 :
			re+=idt[to]
			to-=1
		fr >>= 1
		to >>= 1
		if fr == to :
			re += idt[fr]
			break
	# re += idt[fr]
	print(re)

data = [9,8,1,7,2]
n = 5
base = 1
while base < n : base<<=1
idt = [0]*(base*2)

for k in range(n):
	idt[base+k] = data[k]

for k in range(base-1,0,-1) :
	idt[k] = idt[2*k]+idt[2*k+1]

print(6 & 0)
# update(3,5)
print(idt)
# update(3,1)
# print(idt)
#

RSQ(1,4)
