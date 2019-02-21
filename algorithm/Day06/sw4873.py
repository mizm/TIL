def search() :
    global item
    for i in range(1,len(item)) :
        if item[i] == item[i-1] :
            item = item[:i-1]+item[i+1:]
            search()
            break
for tc in range(int(input())) :
    item = input()
    search()
    print(f'#{tc+1} {len(item)}')