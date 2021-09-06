def solution(weights, head2head):
    dic = {idx:[w,0,0,0] for idx,w in zip(range(1,len(weights) + 1),weights)}
    
    for x in range(1,n := len(head2head)+1):
        for y in range(1,n):
            if head2head[x-1][y-1] == "W":
                dic[x][1] += 1
                if dic[x][0] < dic[y][0]:
                    dic[x][2] += 1
            if head2head[x-1][y-1] != "N":
                dic[x][-1] += 1
        if dic[x][-1]:
            dic[x][1] /= dic[x][-1]
            
    return list(x[0] for x in sorted(dic.items(), key = lambda x: (-x[1][1],-x[1][2],-x[1][0],x[0])))