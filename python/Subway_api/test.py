def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = []
    time = []
    while True :
        if sum(bridge) == 0 and len(truck_weights) == 0:
            break
        if len(truck_weights) > 0 and sum(bridge) + truck_weights[0] <= weight :
            bridge.append(truck_weights.pop(0))
            time.append(bridge_length)
        else :
            plus = 0
            for i in range(len(time)) :
                if time[i] > 0 and plus == 0:
                    plus = time[i]
                elif time[i] > 0 and plus > 0 :
                    plus += 1
                time[i] = 0
                bridge[i] = 0
            answer += plus
            continue
        for i in range(len(time)) :
            time[i] += -1
            if time[i] == 0 :
                bridge[i] = 0
        answer+=1
        print(time,bridge)
    return answer

a =solution(100,100,[10])
print(a)
a =solution(2,10,[7,4,5,6])
print(a)
a =solution(100,100,[10,10,10,10,10,10,10,10,10,10])
print(a)