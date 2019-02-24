def check(ch) :
    op = ['*','+','(',')']
    if ch in op :
        return True
    return False
def stack_push(stack,item) :
    global top
    top += 1
    stack[top] = item
def stack_pop(stack) :
    global top
    item = stack[top]
    stack[top] = 0
    top -= 1
    return item
def t_stack_pop(stack):
    if len(stack) == 0 :
        return False
    else :
        return stack.pop()
def t_stack_push(stack,item) :
    stack.append(item)
def t_cal(data_stack) :
    global top

    # data = ''.join(data_stack)
    # print(data)
    stack = []
    for i in data_stack :
        print(stack)
        if i == '*' or i == '+' or i == '-' or i == '/' or i == '.':
            if i == '.' :
                item = t_stack_pop(stack)
                if item and len(stack) == 0:
                    return item
                else :
                    return "error"
            ans2 = t_stack_pop(stack)
            ans1 = t_stack_pop(stack)
            if ans1 and ans2 :
                if i == '*' :
                    t_stack_push(stack,ans1*ans2)
                elif i == '+' :
                    t_stack_push(stack,ans1+ans2)
                elif i == '/' :
                    t_stack_push(stack,ans1//ans2)
                elif i == '-' :
                    t_stack_push(stack,ans1-ans2)
            else :
                return "error"
        else :
            t_stack_push(stack,int(i))
def calc(data) :
    stack = [0]*(n+1)
    
    for i in data :
        numstack = []
        opstack = []

        if i == ')' :
            while True :
                temp = stack_pop(stack) 
                if temp == "(" :
                    while opstack :
                        numstack.append(opstack.pop(0))
                    numstack.append('.')
                    # print(numstack)
                    stack_push(stack,str(t_cal(numstack)))
                    # print(stack)
                    break
                elif temp == "+" :
                    if '*' in opstack :
                        while opstack :
                            numstack.append(opstack.pop(0))
                    opstack.append(temp)
                elif temp == "*" :
                    opstack.insert(0,temp)
                else :
                    numstack.append(temp)
                    # if "*" in opstack :
                    #     while opstack :
                    #         numstack.append(opstack.pop(0))
            continue
        if check(i) :
            stack_push(stack,i)
        else :
            stack_push(stack,i)
    return stack[0]
for tc in range(10) :
    top = -1
    n = int(input())
    data = input()
    print(f'#{tc+1} {calc(data)}')




        
