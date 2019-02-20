stack = [0] * 100
Info = [0] * 128
Info[ord(")")] = "("
Info[ord("]")] = "["
Info[ord(">")] = "<"
Info[ord("}")] = "{"
data = ">"
def check(data) :
    global stack, Info
    top = -1
    for i in data :
        if i == "(" or i == "<" or i == "{" or i == "[" :
            top += 1
            stack[top] = i
        elif Info[ord(i)] == stack[top] :
            top -= 1
            stack.pop()
        else :
            return False
    if top > -1 :
        return False
    return True

print(check(data))