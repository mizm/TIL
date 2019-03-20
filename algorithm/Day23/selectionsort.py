item = [5,1,2,3]

def rec_selection(s,e) :
	if s == e :
		return
	m = s
	for i in range(s+1,e):
		if item[i] < item[m] :
			m = i
	item[s],item[m] = item[m],item[s]

	rec_selection(s+1,e)

rec_selection(0,4)
print(item)