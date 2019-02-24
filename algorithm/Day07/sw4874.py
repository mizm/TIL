def stack_pop(stack):
    if len(stack) == 0 :
        return False
    else :
        return stack.pop()
def stack_push(stack,item) :
    stack.append(item)
def cal(stack,item) :
    for i in item :
        if i == '*' or i == '+' or i == '-' or i == '/' or i == '.':
            if i == '.' :
                item = stack_pop(stack)
                if item and len(stack) == 0:
                    return item
                else :
                    return "error"
            ans2 = stack_pop(stack)
            ans1 = stack_pop(stack)
            if ans1 and ans2 :
                if i == '*' :
                    stack_push(stack,ans1*ans2)
                elif i == '+' :
                    stack_push(stack,ans1+ans2)
                elif i == '/' :
                    stack_push(stack,ans1//ans2)
                elif i == '-' :
                    stack_push(stack,ans1-ans2)
            else :
                return "error"
        else :
            stack_push(stack,int(i))
#Forth
for tc in range(int(input())) :
    stack = []
    item = input().split()
    print(f'#{tc+1} {cal(stack,item)}')
    