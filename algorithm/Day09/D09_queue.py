front = rear = -1
queue = [0]*10

def enQueue(item) :
    global rear
    rear += 1
    queue[rear] = item

def deQueue() :
    global front
    front += 1
    return queue[front]

for i in range(1,4) :
    enQueue(i)

while front != rear :
    front += 1
    print(queue[front])