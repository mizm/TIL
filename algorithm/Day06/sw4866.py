def search(item) :
    stack = [0]*100
    top = -1
    if not item :
        return 1
    for i in item :
        if i == "{" or i == "(" :
            top += 1
            stack[top]= i
        elif i == "}" or i == ")" :
            if i == "}" and stack[top] != "{":
                return 0
            elif i == ")" and stack[top] != "(" :
                return 0
            else :
                stack[top] = 0
                top -= 1
    if top > -1 :
        return 0
    return 1



for tc in range(int(input())) :
    item = input()
    print(f'#{tc+1} {search(item)}')
