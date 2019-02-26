queue = [0] * 50
front = rear = -1
n = 41
def enQueue(item) :
    global rear
    rear += 1
    queue[rear] = item

def deQueue() :
    global front
    front += 1
    return queue[front]
data = [i for i in range(1,n+1)]
cnt = 0
item = 0
while cnt < n :
    temp = 0
    while temp < 3:
        if data[item] > 0 :
            temp += 1
            if temp == 3 :
                break
        item += 1
        item %= n
    enQueue(data[item])
    data[item] = -1
    item += 1
    item %= n
    cnt+=1
print(queue[rear], queue[rear-1])
